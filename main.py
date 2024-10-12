# ! source fajarkyy

import requests, os
from bs4 import BeautifulSoup
from rich.console import Console
from rich.tree import Tree
console = Console()

headers: dict = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
}

def search(url: str) -> str:
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'lxml')
            contents = soup.find_all('div', class_='css-5wh65g')
            for content in contents:
                a_tag = content.find('a', href=True)
                url = a_tag['href']
                barang_tag = a_tag.find('span', class_='OWkG6oHwAppMn1hIBsC3pQ==')
                harga_tag = a_tag.find('div', class_='ELhJqP-Bfiud3i5eBR8NWg==')
                diskon_tag = a_tag.find('span', class_='_5+V0nr2fU+1eyI2rpS0FYw==')
                toko_tag = a_tag.find('span', class_='X6c-fdwuofj6zGvLKVUaNQ== -9tiTbQgmU1vCjykywQqvA== flip')
                terjual_tag = a_tag.find('span', class_='eLOomHl6J3IWAcdRU8M08A==')
                rate = a_tag.find('span', class_='nBBbPk9MrELbIUbobepKbQ==').get_text(strip=True)
                nama_barang = barang_tag.get_text(strip=True) if barang_tag else None
                harga_barang = harga_tag.get_text(strip=True).split('Rp')[1] if harga_tag else "Tidak tersedia"
                diskon = diskon_tag.get_text(strip=True) if diskon_tag else "Tidak ada diskon"
                offcial = toko_tag.get_text(strip=True) if toko_tag else "Tidak tersedia"
                terjual_ = terjual_tag.get_text(strip=True) if terjual_tag else "Tidak diketahui"
                tree = Tree("")
                xxx = tree.add("Detail product" , style="bold pale_turquoise4")
                xxx.add(f"Nama    : [bold green]{nama_barang}")
                xxx.add(f"Harga   : [bold red]{harga_barang}")
                xxx.add(f"Diskon  : [bold green]{diskon_brng}")
                xxx.add(f"Terjual : [bold green]{terjual_}")
                xxx.add(f"Ranting : [bold green]{rate}")
                xxx.add(f"Toko    : [bold green]{offcial}")
                console.print(tree)
    except AttributeError:pass
            
if __name__ == '__main__':
    os.system('clear')
    keyword = console.input(' [bold green]#[bold white] keyword: ')
    url = 'https://www.tokopedia.com/search?st=&q={}&srp_component_id=02.01.00.00&srp_page_id=&srp_page_title=&navsource='.format(keyword)
    search(url=url)