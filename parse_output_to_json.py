from bs4 import BeautifulSoup
import markdown, json

def parse_output_to_json(message):
    output = message.content
    html = markdown.markdown(output)
    soup = BeautifulSoup(html, 'html.parser')
    code = soup.find('code').text.replace('json\n', '')
    result = json.loads(code)['responses']
    return result
