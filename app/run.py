from alert.alert import AlertSystem as alert
from interpretation.interpretation import Interpreter

def main():

        while True:

            q = input('Pesquisa:')

            if q == 'exit':

                break

            else:

                interpreter = Interpreter()
                value_bool = interpreter.interpret_context(q)

                alerta = alert()
                print(alerta.generate_alert(value_bool))

if __name__ == '__main__':

	main()
