class AlertSystem:

    def __init__(self):

    	self.boolean = False

    # Aqui vamos gerar um alerta, caso seja negativo

    def generate_alert(self, boolean):

        negative_alert_ex = '''

            Cuidado!

            Voce precisa de ajuda? Nao hesite em procurar
            algum amigo ou parente para conversar . 

            Desejamos melhoras : )


        '''

        if boolean == True:

            return negative_alert_ex

    def recomedation_queries(self):

    	pass
