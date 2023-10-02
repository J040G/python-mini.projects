def main():
    print("---Essa é a calculador de pagamentos mensais---")
    print("")
    
    
    principal = float(input("Coloque o preço do imóvel: "))
    apr = float(input("Coloque a taxa de interesse anual: "))
    years = int(input("Coloque a quantidade de meses: "))
    
    monthly_interest_rate = apr/1200
    amount_of_months = years*12
    monthly_payment=principal * monthly_interest_rate/ (1 - (1+ monthly_interest_rate) ** (-amount_of_months))
    
    print("O pagamento mensal desse aluguel é %.2f" % monthly_payment)
    
main()