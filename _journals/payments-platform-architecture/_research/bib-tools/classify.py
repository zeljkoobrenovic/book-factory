# Step 2 of 4: assign each harvested source a topic (the group it is listed under), an evidence type and a company.
# Reads srcs2.json, writes srcs3.json, prints the classification for review (run.sh keeps it in classify-review.txt).
#
# Topics follow the publisher, not the book's parts, because this book weighs a claim by who published the
# source and in what kind of document: the card networks and payment schemes, regulators and standards bodies,
# Stripe (documentation; engineering, blog and newsroom; letters, terms and legal), Adyen (documentation;
# engineering, knowledge hub and newsroom; investor, terms and legal), other companies, and independent
# research, talks and practitioner sources. The evidence types follow the bibliography's thesis in
# journal-spec.json: a regulation or a network rule, an annual report or filing, an annual letter,
# documentation, an engineering post, a press release, a company guide, a secondary source.
# Rules are on the URL, first match wins; corrections for single sources go in fix.py (FIX).
import json, re, os
from urllib.parse import urlparse
HERE = os.path.dirname(os.path.abspath(__file__))
D = json.load(open(os.path.join(HERE, 'srcs2.json')))

TOPICS = ['Card networks, payment schemes and their rules',
          'Regulators, law and standards',
          'Stripe documentation',
          'Stripe engineering, blog and newsroom',
          'Stripe letters, terms and legal',
          'Adyen documentation',
          'Adyen engineering, knowledge hub and newsroom',
          'Adyen investor, terms and legal',
          'Other companies',
          'Research, talks and practitioner sources',
          "The author's planning model"]
NET, REGS, S_DOC, S_ENG, S_LEG, A_DOC, A_ENG, A_LEG, OTHER, PRACT, OWN = range(11)
COMPANY_OF = {NET: 'Card networks and payment schemes', REGS: 'Regulators and standards bodies',
              S_DOC: 'Stripe', S_ENG: 'Stripe', S_LEG: 'Stripe', A_DOC: 'Adyen', A_ENG: 'Adyen', A_LEG: 'Adyen',
              OTHER: 'Other companies', PRACT: 'Independent authors, analysts and press', OWN: 'The author'}

REG, STD, FIL, LET, DOC, TERMS, ENG, PR, GUIDE, SEC, MODEL = (
    'Regulation, law or regulator publication', 'Standard, network rule or scheme publication',
    'Annual report, results or filing', 'Annual letter', 'Product and API documentation',
    'Terms, legal or licence page', 'Engineering post or talk', 'Press release or announcement',
    'Company guide, product page or blog', 'Practitioner or secondary source', "Author's planning model")

def host(s): return urlparse(s['url']).netloc.lower().replace('www.', '') if s['url'] else ''
def has_author(s):  # a named person before the company: "Brandur Leach, Stripe, 2017-02-22"
    return any(re.search(r"\b[A-Z][a-zé]+ (?:van |de )?[A-Z][a-zçé]+", re.sub(
        r"\b(Stripe|Adyen)( [A-Z][a-z]+)*|Knowledge Hub|Black Friday|Cyber Monday|N\.V\.", '', m)) for m in s['metas'])

# (regex on the normalized key without scheme, topic, type); first match wins
RULES = [
    # --- Stripe
    (r'^docs\.stripe\.com/|^support\.stripe\.com/|^stripestatus\.com|^github\.com/stripe', S_DOC, DOC),
    (r'^stripe\.com/annual-updates/', S_LEG, LET),
    (r'^stripe\.com/([a-z-]{2,5}/)?legal/|^stripe\.com/india-data-storage-faq', S_LEG, TERMS),
    (r'^stripe\.com/([a-z-]{2,5}/)?(connect/)?pricing$|^stripe\.com/support-plans', S_LEG, TERMS),
    (r'^stripe\.com/newsroom/', S_ENG, PR),
    (r'^stripe\.com/(rcas|sessions)/|^stripe\.dev/blog/.|^web\.archive\.org/web/\d+/(https://)?(www\.)?stripe\.com/blog/', S_ENG, ENG),
    (r'^stripe\.com/blog/', S_ENG, None),          # ENG when a chapter names the author, else GUIDE
    (r'^stripe\.com/|^stripe\.dev', S_ENG, GUIDE),  # guides, resources, product pages
    (r'^infoq\.com/presentations/(stripe|docdb)', S_ENG, ENG),
    # --- Adyen
    (r'^docs\.adyen\.com/|^help\.adyen\.com/|^status\.adyen\.com|^github\.com/adyen', A_DOC, DOC),
    (r'^investors\.adyen\.com/', A_LEG, FIL),
    (r'^adyen\.com/press-and-media/adyen-(publishes|hosts-investor-day|ipo)', A_LEG, PR),
    (r'^adyen\.com/(legal|licenses|privacy-policy)(/|$)|^adyen\.com/pricing$', A_LEG, TERMS),
    (r'^adyen\.com/press-and-media/', A_ENG, PR),
    (r'^adyen\.com/knowledge-hub/|^medium\.com/adyen/', A_ENG, None),
    (r'^adyen\.com/', A_ENG, GUIDE),
    # --- card networks and payment schemes
    (r'^sec\.gov/archives/edgar/data/0*(1403161|1141391)/', NET, FIL),
    (r'visa\.com/.*(visa-rules-public|interchange-reimbursement|acquirer-mon)', NET, STD),
    (r'visa\.com/.*newsroom|^newsroom\.mastercard\.com', NET, PR),
    (r'visa\.com|mastercard\.(com|us)|^dinersclub\.com|americanexpress\.com|discover\.com', NET, GUIDE),
    (r'^(ideal\.nl|directdebit\.co\.uk|wearepay\.uk|epicompany\.eu|theclearinghouse\.org|nacha\.org|europeanpaymentscouncil\.eu)', NET, STD),
    # --- regulators, law and standards
    (r'^(pcisecuritystandards\.org|blog\.pcisecuritystandards\.org|emvco\.com|ifrs\.org|iso\.org|w3\.org|rfc-editor\.org|datatracker\.ietf\.org)'
     r'|^web\.archive\.org/web/\d+/(https://)?(www\.)?fasb\.org', REGS, STD),
    (r'europa\.eu|^(federalreserve\.gov|frbservices\.org|federalreservehistory\.org|occ\.gov|occ\.treas\.gov|fdic\.gov|fincen\.gov|'
     r'ofac\.treasury\.gov|fca\.org\.uk|csbs\.org|dbf\.georgia\.gov|rbi\.org\.in|govinfo\.gov|law\.cornell\.edu|belastingdienst\.nl|'
     r'consumerfinance\.gov|bankofengland\.co\.uk|dnb\.nl|ecfr\.gov|federalregister\.gov|legislation\.gov\.uk|congress\.gov)', REGS, REG),
    # --- other companies
    (r'^sec\.gov/', OTHER, FIL),
    (r'^(uber\.com/blog|developer\.squareup\.com/blog|medium\.com/airbnb-engineering|aws\.amazon\.com/blogs|'
     r'developers\.googleblog\.com|cloud\.google\.com/blog|checkout\.com/blog|medium\.com/paypal-tech)', OTHER, ENG),
    (r'/newsroom/|/press(-releases?)?/', OTHER, PR),
    (r'^(docs\.|developer\.|developers\.|support\.)|/docs/|/help/|^github\.com/', OTHER, DOC),
    (r'^(paypal\.com|spreedly\.com|primer\.io|gr4vy\.com|paddle\.com|lemonsqueezy\.com|avalara\.com|vertexinc\.com|tempo\.xyz|'
     r'chargebee\.com|moderntreasury\.com|checkout\.com)', OTHER, GUIDE),
]

def classify(s):
    if s['key'] == 'nourl:productscape': return OWN, MODEL
    k = re.sub(r'^https://', '', s['key'])
    for rx, topic, ty in RULES:
        if re.search(rx, k):
            if ty is None: ty = ENG if has_author(s) else GUIDE
            return topic, ty
    return PRACT, SEC  # trade press, law firms, analysts, independent engineers, podcasts

for s in D['srcs']:
    s['topic'], s['type'] = classify(s)
    s['company'] = COMPANY_OF[s['topic']]
json.dump(D, open(os.path.join(HERE, 'srcs3.json'), 'w'), indent=1, ensure_ascii=False)
if __name__ == '__main__':
    for i, T in enumerate(TOPICS):
        print('=====', T, sum(1 for s in D['srcs'] if s['topic'] == i))
        for s in D['srcs']:
            if s['topic'] == i: print('  ', s['type'][:14].ljust(14), '|', s['title'][:60], '|', re.sub(r'^https://', '', s['key'])[:70], '|', s['chapters'][0][:16])
