class BombaCombustivel:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel
    

    def abastecerPorValor(self, valor):
        litros = valor / self.valorLitro

        if self.alterarQuantidadeCombustivel(-litros):
            print(f"O veículo foi abastecido com {litros:.2f}L")
    

    def abastecerPorLitro(self, litros):
        valor = litros * self.valorLitro

        if self.alterarQuantidadeCombustivel(-litros):
            print(f"Você deve pagar com R${valor:.2f}")
    
    
    def alterarValor(self, novoValor):
        self.valorLitro = novoValor
        print(f"O valor do litro de combustível agora é R${novoValor:.2f}.")
    
    
    def alterarCombustivel(self, novoCombustivel):
        self.tipoCombustivel = novoCombustivel
        print(f"O tipo do combustível agora é {novoCombustivel}.")
    
    
    def alterarQuantidadeCombustivel(self, quantidade):
        novaQuantidade = self.quantidadeCombustivel + quantidade

        if novaQuantidade < 0:
            print("Infelizmente a bomba não tem combustível o suficiente.")
            return 0

        self.quantidadeCombustivel = novaQuantidade
        print(f"A nova quantidade de combustível na bomba agora é {novaQuantidade:.2f}L")
        
        return 1