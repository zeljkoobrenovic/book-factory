import json
import datetime

dateString = datetime.date.today().strftime('%Y-%m-%d')

with open('docs/leadership.html', 'w') as html_file:
    data = json.load(open('data/leadership.json'))

    template = open('templates/template.html').read()
    html_file.write(template
                    .replace('${date}', dateString)
                    .replace('${data}', json.dumps(data)))


with open('docs/hard-skills.html', 'w') as html_file:
    data = json.load(open('data/hard-skills.json'))

    template = open('templates/template.html').read()
    html_file.write(template
                    .replace('${date}', dateString)
                    .replace('${data}', json.dumps(data)))

