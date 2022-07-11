import json

__LANGS__ = {
    'py' : 'Python',
    'js' : 'JavaScript',
    'cs' : 'C#',
    'java' : 'Java',
    'c' : 'C',
    'cpp' : 'C++',
    'php' : 'PHP',
    'rb' : 'Ruby',
    'go' : 'Go',
    'swift' : 'Swift',
    'rust' : 'Rust',
}

with open('stealers.json', 'r', encoding='utf-8') as f:
    stealers = json.load(f)
    
with open('STEALERS.md', 'w', encoding='utf-8') as f:
    f.write('# Stealers\n')
    for stealer in stealers:
        stealer = stealers[stealer]
        f.write(f'## {stealer["name"].title()} | Creator: {"Unknown" if stealer["owner"] == "" else stealer["owner"].title()}\n')
        f.write(f"    {'Open' if stealer['open source'] else 'Closed'} source\n")
        f.write(f"    {'Free' if not stealer['paid'] else 'Paid'}\n")
        f.write(f"    Coded with {__LANGS__[stealer['language']]} \n")
        f.write(f"    {'Has' if stealer['resellable'] else 'No'} resale program\n")
        if stealer['resellable']:
            for reseller in stealer['resellers']:
                reseller = stealer['resellers'][reseller]
                f.write(f"    ↳ {reseller['name']}\n")
                f.write(f"        {'Open' if reseller['open source'] else 'Closed'} source\n")
                f.write(f"        {'Free' if not reseller['paid'] else 'Paid'}\n")
                f.write(f"        Coded with {__LANGS__[reseller['language']]} \n")
    