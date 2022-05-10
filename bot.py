import telebot
import mathfunc


bot = telebot.TeleBot("5313397808:AAG6fKq9r8mahbE-PslNUy2yfamhIUAGsKM")


command_list = '''Funções matemáticas:\n
/mdc a b c d ... - MDC(a, b, c, d, ...) - Máximo Divisor Comum.\n
/mmc a b c d ... - MMC(a, b, c, d, ...) - Mínimo Múltiplo Comum.\n
/fator a - Fatoração do número а.\n
/polinomio_add (a₁ + a₂ + .... + a_n) + (b₁ + b₂ + .... + b_n) - Adição de polinômios com coeficientes a₁ + a₂ + .... + a_n e b₁ + b₂ + .... + b_n, onde esses coeficientes começam com a maior potência do polinômio. Se alguma potência não for - escreva '0'. Exemplo, para (2x^5+7x^3-x+14)+(8x^4+11x^3-2) escreva '(2+0+7+0-1+14)+(8+11+0+0-2)'.\n
/polinomio_sub - a mesma coisa, apenas subtração de polinômios. Em vez de '+', escreva '-'.\n
/polinomio_mul (a₁ + a₂ + .... + a_n)*(b₁ + b₂ + .... + b_n) - Multiplicação de polinômios com coeficientes a₁ + a₂ + .... + a_n e b₁ + b₂ + .... + b_n, onde esses coeficientes começam com a maior potência do polinômio. Se alguma potência não é - escreva '0'. 
━━━━━━━━━━━━━━━━
Exemplo, para (2x^5+7x^3-x+14)*(8x^4+11x^3-2) escreva '(2+0+7+0-1+14)*(8+11+0+0-2)'.
━━━━━━━━━━━━━━━━
/polinomio_div - a mesma coisa, apenas divisão de polinômios. Em vez de '*', escreva '/'.\n
/lin_dep a b - Decomposição Linear dos números a e b. A decomposição linear é a*m + b*n = mdc(a, b).\n

Para obter ajuda use /help.'''


error = '''Hm, algo foi escrito errado...
Por favor, use /help para obter a resposta correta.'''


@bot.message_handler(commands=['start'])
def start(message):
    try:
        msg = bot.send_message(message.chat.id, "Olá, eu sou Lyude das Aritmética! Envie aqui suas dúvidas e irei ajudá-lo. Use /help para mais informações")
    except:
        bot.send_message(message.chat.id, "Olá, eu sou Walrider! Envie aqui suas dúvidas e irei ajudá-lo. Use /help para mais informações")
    
    
@bot.message_handler(commands=['help'])
def help(message):
    try:
        msg = bot.send_message(message.chat.id, command_list)
    except:
        bot.send_message(message.chat.id, command_list)
    
    
@bot.message_handler(commands=['mdc'])
def gcd(message):
    try:
        msg = f'{message.text}'
        answer = bot.send_message(message.chat.id, mathfunc.gcd(msg))
    except:
        bot.send_message(message.chat.id, error)
    
    
@bot.message_handler(commands=['mmc'])
def lcm(message):
    try:
        msg = f'{message.text}'
        answer = bot.send_message(message.chat.id, mathfunc.lcm(msg))
    except:
        bot.send_message(message.chat.id, error)
    
    
@bot.message_handler(commands=['fator'])
def factor(message):
    try:
        msg = f'{message.text}'
        answer = bot.send_message(message.chat.id, mathfunc.factor(msg))
    except:
        bot.send_message(message.chat.id, error)

        
@bot.message_handler(commands=['polinomio_add'])
def polynoms_add(message):
    try:
        msg = f'{message.text}'
        answer = bot.send_message(message.chat.id, mathfunc.polynoms_add(msg))
    except:
        bot.send_message(message.chat.id, error)
    
    
@bot.message_handler(commands=['polinomio_sub'])
def polynoms_sub(message):
    try:
        msg = f'{message.text}'
        answer = bot.send_message(message.chat.id, mathfunc.polynoms_sub(msg))
    except:
        bot.send_message(message.chat.id, error)
    
    
@bot.message_handler(commands=['polinomio_mul'])
def polynoms_mul(message):
    try:
        msg = f'{message.text}'
        answer = bot.send_message(message.chat.id, mathfunc.polynoms_mul(msg))
    except:
        bot.send_message(message.chat.id, error)
    
    
@bot.message_handler(commands=['polinomio_div'])
def polynoms_div(message):
    try:
        msg = f'{message.text}'
        answer = bot.send_message(message.chat.id, mathfunc.polynoms_div(msg))
    except:
        bot.send_message(message.chat.id, error)
    
    
@bot.message_handler(commands=['lin_dep'])
def lin_dep(message):
    try:
        msg = f'{message.text}'
        answer = bot.send_message(message.chat.id, mathfunc.lin_dep(msg))
    except:
        bot.send_message(message.chat.id, error)
        

bot.polling()
