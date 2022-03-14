# BIBLIOTECAS
#-----------------------
import twilioDados as dzn
from twilio.rest import Client
#-----------------------
# FUNÇÕES
#-----------------------
def inicializar(sid,token) -> Client:
    cliente = Client(sid,token);
    return cliente;

def mandarMensagem(cliente:Client,numberTwilio:str,numberClient:str,mensagem:str) -> None:
    sms = cliente.messages.create(
        from_=numberTwilio,
        to=numberClient,
        body=mensagem
    );

def mandarMensagemWpp(cliente:Client,numberTwilio:str,numberClient:str,mensagem:str) -> None:
    wpp = cliente.messages.create(
        from_=numberTwilio,
        to=numberClient,
        body=mensagem
    );

def fazerCall(cliente:Client,numberTwilio:str,numberClient:str,mensagem:str) -> None:
    call = cliente.calls.create(
        from_=numberTwilio,
        to=numberClient,
        twiml=mensagem
    );
#-----------------------
# M A I N ()
#-----------------------
if __name__ == '__main__':
    # Informações da conta
    accountSID = dzn.accountSID;
    authToken = dzn.authToken;
    # Numeros de telefone
    numeros = dzn.numeros;
    numeroTwilio = dzn.numeroTwilio;
    # Numeros de Whatsapp
    numerosWPP = dzn.numerosWhatsapp;
    # Numero Twilio de Whatsapp
    numeroTwilioWPP = dzn.numeroTwilioWhatsapp;
    # Mensagens
    mensagemSMS="Horário do Remédio 😁💊";
    mensagemLigacao="""
                        <Response>
                        <Say language="pt-BR">
                            Olá, Boa noite! está no horário do remédio! Tchau e beijos.
                        </Say>
                        </Response>
                    """;
    # Execução
    cliente = inicializar(accountSID,authToken);
    # Ligação e mensagens
    for numero in numeros:
        mandarMensagem( cliente=cliente,
                        numberTwilio=numeroTwilio,
                        numberClient=numero,
                        mensagem=mensagemSMS);
        fazerCall(  cliente=cliente,
                    numberTwilio=numeroTwilio,
                    numberClient=numero,
                    mensagem=mensagemLigacao);
    # Mensagens de Whatsapp
    for numero in numerosWPP:
        mandarMensagemWpp(  cliente=cliente,
                            numberTwilio=numeroTwilioWPP,
                            numberClient=numero,
                            mensagem=mensagemSMS);
#-----------------------