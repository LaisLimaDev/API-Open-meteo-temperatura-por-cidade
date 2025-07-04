from .core import get_temperatures_for_cities

def main():
    cidades = input("Digite os nomes das cidades separados por vírgula: ")
    lista_cidades = [c.strip() for c in cidades.split(",")]
    get_temperatures_for_cities(lista_cidades)

if __name__ == "__main__":
    main()