import smtplib 
import email.message

def enviar_email():
    corpo_email = """
    <p>Olá Usuário</p>
    <p>AAqui estão os indicadores mais recentes:</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Indicadores"
    msg['From'] = 'projetosenai.cd24@gmail.com'
    msg['To'] = 'clodoaldo.batista.s@gmail.com, eliane.bdsantos@gmail.com'
    password = "cdol xorh tmlf inpz"
    msg.add_header('Contect-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com:587')
    s.starttls()
    s.login(msg['From'],password)
    s.sendmail(msg['From'], msg['To'].split(','), msg.as_string().encode('utf-8'))
    print('Email enviado')
    
if __name__ == "__main__":
    enviar_email()