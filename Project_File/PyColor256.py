# PROJETO DE COLORIR TEXTOS ALEATÓRIOS VISTO QUE O OUTRO NÃO DEU CERTO...

'''# AZUL
blue1 = '\033[38;5;17m'
blue2 = '\033[38;5;18m'
blue3 = '\033[38;5;19m'
blue4 = '\033[38;5;20m'
blue5 = '\033[38;5;21m'
# ROXO
purple1 = '\033[38;5;53m'
purple2 = '\033[38;5;54m'
purple3 = '\033[38;5;55m'
purple4 = '\033[38;5;56m'
purple5 = '\033[38;5;57m'
# VERDE
green1 = '\033[38;5;82m'
green2 = '\033[38;5;83m'
green3 = '\033[38;5;84m'
green4 = '\033[38;5;85m'
green5 = '\033[38;5;86m'
green6 = '\033[38;5;87m'
# AMARELO
yellow1 = '\033[38;5;226m'
yellow2 = '\033[38;5;227m'
yellow3 = '\033[38;5;228m'
yellow4 = '\033[38;5;229m'
yellow5 = '\033[38;5;230m'
# VERMELHO
red1 = '\033[38;5;196m'
red2 = '\033[38;5;197m'
red3 = '\033[38;5;198m'
red4 = '\033[38;5;199m'
red5 = '\033[38;5;200m'
red6 = '\033[38;5;201m'
# SLA KKK
mid1 = '\033[38;5;46m'
mid2 = '\033[38;5;47m'
mid3 = '\033[38;5;48m'
mid4 = '\033[38;5;49m'
mid5 = '\033[38;5;50m'
mid6 = '\033[38;5;51m'

f"""
{mid1}T{mid2}H{mid3}A{mid4}N{mid5}K{mid6}S 
{blue1}F{blue2}O{blue3}R 
{yellow1}U{yellow2}S{yellow3}I{yellow4}N{yellow5}G 
{red1}M{red2}Y 
{green1}C{green2}O{green3}L{green4}O{green5}R 
{red1}M{red2}O{red3}D{red4}U{red5}L{red6}E!
"""'''

def by_VRC():
    light_red = '\033[1;91m'
    red = '\033[1;31m'
    light_yellow = '\033[1;93m'
    yellow = '\033[1;33m'
    light_green = '\033[1;92m'
    green = '\033[1;32m'
    light_blue = '\033[1;94m'
    blue = '\033[1;34m'
    light_cyan = '\033[1;96m'
    cyan = '\033[1;36m'
    light_magenta = '\033[1;95m'
    magenta = '\033[1;35m'

    dic_color = [
        light_red, light_red, red, red, light_yellow, light_yellow, yellow, yellow, green, green, light_green,
        light_green,
        light_blue, light_blue, blue, blue, cyan, cyan,
        light_cyan, light_cyan, light_magenta, light_magenta,
        magenta, magenta, light_red, light_red, red, red, light_yellow, light_yellow, yellow, yellow, green, green,
        light_green, light_green,
        light_blue, light_blue, blue, blue, cyan, cyan,
        light_cyan, light_cyan, light_magenta, light_magenta,
        magenta, magenta, light_red, light_red, red, red, light_yellow, light_yellow, yellow, yellow, green, green,
        light_green, light_green,
        light_blue, light_blue, blue, blue, cyan, cyan,
        light_cyan, light_cyan, light_magenta, light_magenta,
        magenta, magenta]

    from math import ceil

    # LISTA DE CORES

    txt = (rf''' 
    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓   
    ┃ ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ ┃  
    ┃ ░░                                     /   \                                     ░░ ┃ 
    ┃ ░░    _                        )      ((   ))     (                              ░░ ┃ 
    ┃ ░░   (@)                      /|\      ))_((     /|\                             ░░ ┃ 
    ┃ ░░   |-|                     / | \    (/\|/\)   / | \                      (@)   ░░ ┃ 
    ┃ ░░   | | -------------------/--|-voV---\`|'/--Vov-|--\---------------------|-|   ░░ ┃ 
    ┃ ░░   |-|                         '^`   (o o)  '^`                          | |   ░░ ┃ 
    ┃ ░░   | |                               `\Y/'                               |-|   ░░ ┃ 
    ┃ ░░   |-|                  !TANKS FOR USING MY COLOR MODULE!                | |   ░░ ┃ 
    ┃ ░░   | |                        BY DR MIDNIGHT / VRC                       |-|   ░░ ┃ 
    ┃ ░░   |-|                           Vinícius Coral                          | |   ░░ ┃ 
    ┃ ░░   | |                     https://github.com/MidD3Vil                   |-|   ░░ ┃ 
    ┃ ░░   |_|___________________________________________________________________| |   ░░ ┃   
    ┃ ░░   (@)              l   /\ /         ( (       \ /\   l                `\|-|   ░░ ┃ 
    ┃ ░░                    l /   V           \ \       V   \ l                  (@)   ░░ ┃ 
    ┃ ░░                    l/                _) )_          \I                        ░░ ┃  
    ┃ ░░                                     `\ /'                                     ░░ ┃                                                                             
    ┃ ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ ┃ 
    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
    ''').strip()

    print('\n')
    split = txt.split(None, 16)  # Tudo
    split_line = txt.split('\n')
    num_lines = len(split_line)  # Numero de \n

    process_number = 0
    count = -1

    for c in range(num_lines):
        print('')
        # PEGAR A 1 LINHA
        line1 = split_line[process_number]  # Linha 1

        # DIVIDIR 1 LINHA POR 12
        num_line1 = len(line1)  # Num de caracteres da 1 linha
        num_line1_12 = ceil(num_line1 / 16)  # Num de caracteres da 1 linha / 12

        # CRIAR LISTA COM A 1 LINHA CORTADA DE 12 EM 12
        replace_order = 1
        replace_order_1 = 0

        plus_fim = num_line1_12
        plus_inicio = 0
        list12 = []
        for c in range(16):
            list12.append(line1[plus_inicio:plus_fim])
            plus_fim += num_line1_12
            plus_inicio += num_line1_12

        # DEGRADE DA 1 LINHA
        list12_count = 0
        color = 'mid.vrc'
        count += 1
        for c in range(16):
            color = dic_color[count]
            count += 1
            # print('\n{:{}}'.format(f'{color}■'*div_line, num_line), end='')
            print(f'{color}{list12[list12_count]}', end='')
            list12_count += 1
        process_number += 1
        count -= 16
    return ''
    # FAZER TODO O PROCESSO PARA AS OUTRAS LINHAS

def all_colors(word, color):
    if color == '0':
        return f'\033[38;5;0m{word}'

    elif color == '1':
        return f'\033[38;5;1m{word}'

    elif color == '2':
        return f'\033[38;5;2m{word}'

    elif color == '3':
        return f'\033[38;5;3m{word}'

    elif color == '4':
        return f'\033[38;5;4m{word}'

    elif color == '5':
        return f'\033[38;5;5m{word}'

    elif color == '6':
        return f'\033[38;5;6m{word}'

    elif color == '7':
        return f'\033[38;5;7m{word}'

    elif color == '8':
        return f'\033[38;5;8m{word}'

    elif color == '9':
        return f'\033[38;5;9m{word}'

    elif color == '10':
        return f'\033[38;5;10m{word}'

    elif color == '11':
        return f'\033[38;5;11m{word}'

    elif color == '12':
        return f'\033[38;5;12m{word}'

    elif color == '13':
        return f'\033[38;5;13m{word}'

    elif color == '14':
        return f'\033[38;5;14m{word}'

    elif color == '15':
        return f'\033[38;5;15m{word}'

    elif color == '16':
        return f'\033[38;5;16m{word}'

    elif color == '17':
        return f'\033[38;5;17m{word}'

    elif color == '18':
        return f'\033[38;5;18m{word}'

    elif color == '19':
        return f'\033[38;5;19m{word}'

    elif color == '20':
        return f'\033[38;5;20m{word}'

    elif color == '21':
        return f'\033[38;5;21m{word}'

    elif color == '22':
        return f'\033[38;5;22m{word}'

    elif color == '23':
        return f'\033[38;5;23m{word}'

    elif color == '24':
        return f'\033[38;5;24m{word}'

    elif color == '25':
        return f'\033[38;5;25m{word}'

    elif color == '26':
        return f'\033[38;5;26m{word}'

    elif color == '27':
        return f'\033[38;5;27m{word}'

    elif color == '28':
        return f'\033[38;5;28m{word}'

    elif color == '29':
        return f'\033[38;5;29m{word}'

    elif color == '30':
        return f'\033[38;5;30m{word}'

    elif color == '31':
        return f'\033[38;5;31m{word}'

    elif color == '32':
        return f'\033[38;5;32m{word}'

    elif color == '33':
        return f'\033[38;5;33m{word}'

    elif color == '34':
        return f'\033[38;5;34m{word}'

    elif color == '35':
        return f'\033[38;5;35m{word}'

    elif color == '36':
        return f'\033[38;5;36m{word}'

    elif color == '37':
        return f'\033[38;5;37m{word}'

    elif color == '38':
        return f'\033[38;5;38m{word}'

    elif color == '39':
        return f'\033[38;5;39m{word}'

    elif color == '40':
        return f'\033[38;5;40m{word}'

    elif color == '41':
        return f'\033[38;5;41m{word}'

    elif color == '42':
        return f'\033[38;5;42m{word}'

    elif color == '43':
        return f'\033[38;5;43m{word}'

    elif color == '44':
        return f'\033[38;5;44m{word}'

    elif color == '45':
        return f'\033[38;5;45m{word}'

    elif color == '46':
        return f'\033[38;5;46m{word}'

    elif color == '47':
        return f'\033[38;5;47m{word}'

    elif color == '48':
        return f'\033[38;5;48m{word}'

    elif color == '49':
        return f'\033[38;5;49m{word}'

    elif color == '50':
        return f'\033[38;5;50m{word}'

    elif color == '51':
        return f'\033[38;5;51m{word}'

    elif color == '52':
        return f'\033[38;5;52m{word}'

    elif color == '53':
        return f'\033[38;5;53m{word}'

    elif color == '54':
        return f'\033[38;5;54m{word}'

    elif color == '55':
        return f'\033[38;5;55m{word}'

    elif color == '56':
        return f'\033[38;5;56m{word}'

    elif color == '57':
        return f'\033[38;5;57m{word}'

    elif color == '58':
        return f'\033[38;5;58m{word}'

    elif color == '59':
        return f'\033[38;5;59m{word}'

    elif color == '60':
        return f'\033[38;5;60m{word}'

    elif color == '61':
        return f'\033[38;5;61m{word}'

    elif color == '62':
        return f'\033[38;5;62m{word}'

    elif color == '63':
        return f'\033[38;5;63m{word}'

    elif color == '64':
        return f'\033[38;5;64m{word}'

    elif color == '65':
        return f'\033[38;5;65m{word}'

    elif color == '66':
        return f'\033[38;5;66m{word}'

    elif color == '67':
        return f'\033[38;5;67m{word}'

    elif color == '68':
        return f'\033[38;5;68m{word}'

    elif color == '69':
        return f'\033[38;5;69m{word}'

    elif color == '70':
        return f'\033[38;5;70m{word}'

    elif color == '71':
        return f'\033[38;5;71m{word}'

    elif color == '72':
        return f'\033[38;5;72m{word}'

    elif color == '73':
        return f'\033[38;5;73m{word}'

    elif color == '74':
        return f'\033[38;5;74m{word}'

    elif color == '75':
        return f'\033[38;5;75m{word}'

    elif color == '76':
        return f'\033[38;5;76m{word}'

    elif color == '77':
        return f'\033[38;5;77m{word}'

    elif color == '78':
        return f'\033[38;5;78m{word}'

    elif color == '79':
        return f'\033[38;5;79m{word}'

    elif color == '80':
        return f'\033[38;5;80m{word}'

    elif color == '81':
        return f'\033[38;5;81m{word}'

    elif color == '82':
        return f'\033[38;5;82m{word}'

    elif color == '83':
        return f'\033[38;5;83m{word}'

    elif color == '84':
        return f'\033[38;5;84m{word}'

    elif color == '85':
        return f'\033[38;5;85m{word}'

    elif color == '86':
        return f'\033[38;5;86m{word}'

    elif color == '87':
        return f'\033[38;5;87m{word}'

    elif color == '88':
        return f'\033[38;5;88m{word}'

    elif color == '89':
        return f'\033[38;5;89m{word}'

    elif color == '90':
        return f'\033[38;5;90m{word}'

    elif color == '91':
        return f'\033[38;5;91m{word}'

    elif color == '92':
        return f'\033[38;5;92m{word}'

    elif color == '93':
        return f'\033[38;5;93m{word}'

    elif color == '94':
        return f'\033[38;5;94m{word}'

    elif color == '95':
        return f'\033[38;5;95m{word}'

    elif color == '96':
        return f'\033[38;5;96m{word}'

    elif color == '97':
        return f'\033[38;5;97m{word}'

    elif color == '98':
        return f'\033[38;5;98m{word}'

    elif color == '99':
        return f'\033[38;5;99m{word}'

    elif color == '100':
        return f'\033[38;5;100m{word}'

    elif color == '101':
        return f'\033[38;5;101m{word}'

    elif color == '102':
        return f'\033[38;5;102m{word}'

    elif color == '103':
        return f'\033[38;5;103m{word}'

    elif color == '104':
        return f'\033[38;5;104m{word}'

    elif color == '105':
        return f'\033[38;5;105m{word}'

    elif color == '106':
        return f'\033[38;5;106m{word}'

    elif color == '107':
        return f'\033[38;5;107m{word}'

    elif color == '108':
        return f'\033[38;5;108m{word}'

    elif color == '109':
        return f'\033[38;5;109m{word}'

    elif color == '110':
        return f'\033[38;5;110m{word}'

    elif color == '111':
        return f'\033[38;5;111m{word}'

    elif color == '112':
        return f'\033[38;5;112m{word}'

    elif color == '113':
        return f'\033[38;5;113m{word}'

    elif color == '114':
        return f'\033[38;5;114m{word}'

    elif color == '115':
        return f'\033[38;5;115m{word}'

    elif color == '116':
        return f'\033[38;5;116m{word}'

    elif color == '117':
        return f'\033[38;5;117m{word}'

    elif color == '118':
        return f'\033[38;5;118m{word}'

    elif color == '119':
        return f'\033[38;5;119m{word}'

    elif color == '120':
        return f'\033[38;5;120m{word}'

    elif color == '121':
        return f'\033[38;5;121m{word}'

    elif color == '122':
        return f'\033[38;5;122m{word}'

    elif color == '123':
        return f'\033[38;5;123m{word}'

    elif color == '124':
        return f'\033[38;5;124m{word}'

    elif color == '125':
        return f'\033[38;5;125m{word}'

    elif color == '126':
        return f'\033[38;5;126m{word}'

    elif color == '127':
        return f'\033[38;5;127m{word}'

    elif color == '128':
        return f'\033[38;5;128m{word}'

    elif color == '129':
        return f'\033[38;5;129m{word}'

    elif color == '130':
        return f'\033[38;5;130m{word}'

    elif color == '131':
        return f'\033[38;5;131m{word}'

    elif color == '132':
        return f'\033[38;5;132m{word}'

    elif color == '133':
        return f'\033[38;5;133m{word}'

    elif color == '134':
        return f'\033[38;5;134m{word}'

    elif color == '135':
        return f'\033[38;5;135m{word}'

    elif color == '136':
        return f'\033[38;5;136m{word}'

    elif color == '137':
        return f'\033[38;5;137m{word}'

    elif color == '138':
        return f'\033[38;5;138m{word}'

    elif color == '139':
        return f'\033[38;5;139m{word}'

    elif color == '140':
        return f'\033[38;5;140m{word}'

    elif color == '141':
        return f'\033[38;5;141m{word}'

    elif color == '142':
        return f'\033[38;5;142m{word}'

    elif color == '143':
        return f'\033[38;5;143m{word}'

    elif color == '144':
        return f'\033[38;5;144m{word}'

    elif color == '145':
        return f'\033[38;5;145m{word}'

    elif color == '146':
        return f'\033[38;5;146m{word}'

    elif color == '147':
        return f'\033[38;5;147m{word}'

    elif color == '148':
        return f'\033[38;5;148m{word}'

    elif color == '149':
        return f'\033[38;5;149m{word}'

    elif color == '150':
        return f'\033[38;5;150m{word}'

    elif color == '151':
        return f'\033[38;5;151m{word}'

    elif color == '152':
        return f'\033[38;5;152m{word}'

    elif color == '153':
        return f'\033[38;5;153m{word}'

    elif color == '154':
        return f'\033[38;5;154m{word}'

    elif color == '155':
        return f'\033[38;5;155m{word}'

    elif color == '156':
        return f'\033[38;5;156m{word}'

    elif color == '157':
        return f'\033[38;5;157m{word}'

    elif color == '158':
        return f'\033[38;5;158m{word}'

    elif color == '159':
        return f'\033[38;5;159m{word}'

    elif color == '160':
        return f'\033[38;5;160m{word}'

    elif color == '161':
        return f'\033[38;5;161m{word}'

    elif color == '162':
        return f'\033[38;5;162m{word}'

    elif color == '163':
        return f'\033[38;5;163m{word}'

    elif color == '164':
        return f'\033[38;5;164m{word}'

    elif color == '165':
        return f'\033[38;5;165m{word}'

    elif color == '166':
        return f'\033[38;5;166m{word}'

    elif color == '167':
        return f'\033[38;5;167m{word}'

    elif color == '168':
        return f'\033[38;5;168m{word}'

    elif color == '169':
        return f'\033[38;5;169m{word}'

    elif color == '170':
        return f'\033[38;5;170m{word}'

    elif color == '171':
        return f'\033[38;5;171m{word}'

    elif color == '172':
        return f'\033[38;5;172m{word}'

    elif color == '173':
        return f'\033[38;5;173m{word}'

    elif color == '174':
        return f'\033[38;5;174m{word}'

    elif color == '175':
        return f'\033[38;5;175m{word}'

    elif color == '176':
        return f'\033[38;5;176m{word}'

    elif color == '177':
        return f'\033[38;5;177m{word}'

    elif color == '178':
        return f'\033[38;5;178m{word}'

    elif color == '179':
        return f'\033[38;5;179m{word}'

    elif color == '180':
        return f'\033[38;5;180m{word}'

    elif color == '181':
        return f'\033[38;5;181m{word}'

    elif color == '182':
        return f'\033[38;5;182m{word}'

    elif color == '183':
        return f'\033[38;5;183m{word}'

    elif color == '184':
        return f'\033[38;5;184m{word}'

    elif color == '185':
        return f'\033[38;5;185m{word}'

    elif color == '187':
        return f'\033[38;5;186m{word}'

    elif color == '188':
        return f'\033[38;5;188m{word}'

    elif color == '189':
        return f'\033[38;5;189m{word}'

    elif color == '190':
        return f'\033[38;5;190m{word}'

    elif color == '191':
        return f'\033[38;5;191m{word}'

    elif color == '192':
        return f'\033[38;5;192m{word}'

    elif color == '193':
        return f'\033[38;5;193m{word}'

    elif color == '194':
        return f'\033[38;5;194m{word}'

    elif color == '195':
        return f'\033[38;5;195m{word}'

    elif color == '196':
        return f'\033[38;5;196m{word}'

    elif color == '197':
        return f'\033[38;5;197m{word}'

    elif color == '198':
        return f'\033[38;5;198m{word}'

    elif color == '199':
        return f'\033[38;5;199m{word}'

    elif color == '200':
        return f'\033[38;5;200m{word}'

    elif color == '201':
        return f'\033[38;5;201m{word}'

    elif color == '202':
        return f'\033[38;5;202m{word}'

    elif color == '203':
        return f'\033[38;5;203m{word}'

    elif color == '204':
        return f'\033[38;5;204m{word}'

    elif color == '205':
        return f'\033[38;5;205m{word}'

    elif color == '206':
        return f'\033[38;5;206m{word}'

    elif color == '207':
        return f'\033[38;5;207m{word}'

    elif color == '208':
        return f'\033[38;5;208m{word}'

    elif color == '209':
        return f'\033[38;5;209m{word}'

    elif color == '210':
        return f'\033[38;5;210m{word}'

    elif color == '211':
        return f'\033[38;5;211m{word}'

    elif color == '212':
        return f'\033[38;5;212m{word}'

    elif color == '213':
        return f'\033[38;5;213m{word}'

    elif color == '214':
        return f'\033[38;5;214m{word}'

    elif color == '215':
        return f'\033[38;5;215m{word}'

    elif color == '216':
        return f'\033[38;5;216m{word}'

    elif color == '217':
        return f'\033[38;5;217m{word}'

    elif color == '218':
        return f'\033[38;5;218m{word}'

    elif color == '219':
        return f'\033[38;5;219m{word}'

    elif color == '220':
        return f'\033[38;5;220m{word}'

    elif color == '221':
        return f'\033[38;5;221m{word}'

    elif color == '222':
        return f'\033[38;5;222m{word}'

    elif color == '223':
        return f'\033[38;5;223m{word}'

    elif color == '224':
        return f'\033[38;5;224m{word}'

    elif color == '225':
        return f'\033[38;5;225m{word}'

    elif color == '226':
        return f'\033[38;5;226m{word}'

    elif color == '227':
        return f'\033[38;5;227m{word}'

    elif color == '228':
        return f'\033[38;5;228m{word}'

    elif color == '229':
        return f'\033[38;5;229m{word}'

    elif color == '230':
        return f'\033[38;5;230m{word}'

    elif color == '231':
        return f'\033[38;5;231m{word}'

    elif color == '232':
        return f'\033[38;5;232m{word}'

    elif color == '233':
        return f'\033[38;5;233m{word}'

    elif color == '234':
        return f'\033[38;5;234m{word}'

    elif color == '235':
        return f'\033[38;5;235m{word}'

    elif color == '236':
        return f'\033[38;5;236m{word}'

    elif color == '237':
        return f'\033[38;5;237m{word}'

    elif color == '238':
        return f'\033[38;5;238m{word}'

    elif color == '239':
        return f'\033[38;5;239m{word}'

    elif color == '240':
        return f'\033[38;5;240m{word}'

    elif color == '241':
        return f'\033[38;5;241m{word}'

    elif color == '242':
        return f'\033[38;5;242m{word}'

    elif color == '243':
        return f'\033[38;5;243m{word}'

    elif color == '244':
        return f'\033[38;5;244m{word}'

    elif color == '245':
        return f'\033[38;5;245m{word}'

    elif color == '246':
        return f'\033[38;5;246m{word}'

    elif color == '247':
        return f'\033[38;5;247m{word}'

    elif color == '248':
        return f'\033[38;5;248m{word}'

    elif color == '249':
        return f'\033[38;5;249m{word}'

    elif color == '250':
        return f'\033[38;5;250m{word}'

    elif color == '251':
        return f'\033[38;5;251m{word}'

    elif color == '252':
        return f'\033[38;5;252m{word}'

    elif color == '253':
        return f'\033[38;5;253m{word}'

    elif color == '254':
        return f'\033[38;5;254m{word}'

    elif color == '255':
        return f'\033[38;5;255m{word}'













def light_red(word):
    Mlight_redM = '\033[1;91m'
    return f'{Mlight_redM}{word}'
def red(word):
    Mlight_redM = '\033[1;31m'
    return f'{Mlight_redM}{word}'
def light_yellow(word):
    Dlight_yellowD = '\033[1;93m'
    return f'{Dlight_yellowD}{word}'
def yellow(word):
    NyellowN = '\033[1;33m'
    return f'{NyellowN}{word}'
def light_green(word):
    Ilight_greenI = '\033[1;92m'
    return f'{Ilight_greenI}{word}'
def green(word):
    GgreenG = '\033[1;32m'
    return f'{GgreenG}{word}'
def light_blue(word):
    Hlight_blueH = '\033[1;94m'
    return f'{Hlight_blueH}{word}'
def blue(word):
    TblueT = '\033[1;34m'
    return f'{TblueT}{word}'
def light_cyan(word):
    Vlight_cyanV = '\033[1;96m'
    return f'{Vlight_cyanV}{word}'
def cyan(word):
    IcyanI = '\033[1;36m'
    print()
    return f'{IcyanI}{word}'
def light_purple(word):
    Nlight_purpleN = '\033[1;95m'
    return f'{Nlight_purpleN}{word}'
def purple(word):
    IpurpleI = '\033[1;35m'
    return f'{IpurpleI}{word}'


def white(word):
    CwhiteC = '\033[1;97m'
    return f'{CwhiteC}{word}'
def light_gray(word):
    Ilight_grayI = '\033[1;37m'
    return f'{Ilight_grayI}{word}'
def dark_gray(word):
    Udark_grayU = '\033[1;90m'
    return f'{Udark_grayU}{word}'
def black(word):
    SblackS = '\033[1;30m'
    return f'{SblackS}{word}'


def list_colors():
    set = '▓▓ 🡲 '
    return f'''
    \033[38;5;0m {set} 0     \033[38;5;65m {set} 65    \033[38;5;130m {set} 130    \033[38;5;195m {set} 195
    \033[38;5;1m {set} 1     \033[38;5;66m {set} 66    \033[38;5;131m {set} 131    \033[38;5;196m {set} 196
    \033[38;5;2m {set} 2     \033[38;5;67m {set} 67    \033[38;5;132m {set} 132    \033[38;5;197m {set} 197
    \033[38;5;3m {set} 3     \033[38;5;68m {set} 68    \033[38;5;133m {set} 133    \033[38;5;198m {set} 198
    \033[38;5;4m {set} 4     \033[38;5;69m {set} 69    \033[38;5;134m {set} 134    \033[38;5;199m {set} 199
    \033[38;5;5m {set} 5     \033[38;5;70m {set} 70    \033[38;5;135m {set} 135    \033[38;5;200m {set} 200
    \033[38;5;6m {set} 6     \033[38;5;71m {set} 71    \033[38;5;136m {set} 136    \033[38;5;201m {set} 201
    \033[38;5;7m {set} 7     \033[38;5;72m {set} 72    \033[38;5;137m {set} 137    \033[38;5;202m {set} 202
    \033[38;5;8m {set} 8     \033[38;5;73m {set} 73    \033[38;5;138m {set} 138    \033[38;5;203m {set} 203
    \033[38;5;9m {set} 9     \033[38;5;74m {set} 74    \033[38;5;139m {set} 139    \033[38;5;204m {set} 204
    \033[38;5;10m {set} 10    \033[38;5;75m {set} 75    \033[38;5;140m {set} 140    \033[38;5;205m {set} 205
    \033[38;5;11m {set} 11    \033[38;5;76m {set} 76    \033[38;5;141m {set} 141    \033[38;5;206m {set} 206
    \033[38;5;12m {set} 12    \033[38;5;77m {set} 77    \033[38;5;142m {set} 142    \033[38;5;207m {set} 207
    \033[38;5;13m {set} 13    \033[38;5;78m {set} 78    \033[38;5;143m {set} 143    \033[38;5;208m {set} 208
    \033[38;5;14m {set} 14    \033[38;5;79m {set} 79    \033[38;5;144m {set} 144    \033[38;5;209m {set} 209
    \033[38;5;15m {set} 15    \033[38;5;80m {set} 80    \033[38;5;145m {set} 145    \033[38;5;210m {set} 210
    \033[38;5;16m {set} 16    \033[38;5;81m {set} 81    \033[38;5;146m {set} 146    \033[38;5;211m {set} 211
    \033[38;5;17m {set} 17    \033[38;5;82m {set} 82    \033[38;5;147m {set} 147    \033[38;5;212m {set} 212
    \033[38;5;18m {set} 18    \033[38;5;83m {set} 83    \033[38;5;148m {set} 148    \033[38;5;213m {set} 213
    \033[38;5;19m {set} 19    \033[38;5;84m {set} 84    \033[38;5;149m {set} 149    \033[38;5;214m {set} 214
    \033[38;5;20m {set} 20    \033[38;5;85m {set} 85    \033[38;5;150m {set} 150    \033[38;5;215m {set} 215
    \033[38;5;21m {set} 21    \033[38;5;86m {set} 86    \033[38;5;151m {set} 151    \033[38;5;216m {set} 216
    \033[38;5;22m {set} 22    \033[38;5;87m {set} 87    \033[38;5;152m {set} 152    \033[38;5;217m {set} 217
    \033[38;5;23m {set} 23    \033[38;5;88m {set} 88    \033[38;5;153m {set} 153    \033[38;5;218m {set} 218
    \033[38;5;24m {set} 24    \033[38;5;89m {set} 89    \033[38;5;154m {set} 154    \033[38;5;219m {set} 219
    \033[38;5;25m {set} 25    \033[38;5;90m {set} 90    \033[38;5;155m {set} 155    \033[38;5;220m {set} 220
    \033[38;5;26m {set} 26    \033[38;5;91m {set} 91    \033[38;5;156m {set} 156    \033[38;5;221m {set} 221
    \033[38;5;27m {set} 27    \033[38;5;92m {set} 92    \033[38;5;157m {set} 157    \033[38;5;222m {set} 222
    \033[38;5;28m {set} 28    \033[38;5;93m {set} 93    \033[38;5;158m {set} 158    \033[38;5;223m {set} 223
    \033[38;5;29m {set} 29    \033[38;5;94m {set} 94    \033[38;5;159m {set} 159    \033[38;5;224m {set} 224
    \033[38;5;30m {set} 30    \033[38;5;95m {set} 95    \033[38;5;160m {set} 160    \033[38;5;225m {set} 225
    \033[38;5;31m {set} 31    \033[38;5;96m {set} 96    \033[38;5;161m {set} 161    \033[38;5;226m {set} 226
    \033[38;5;32m {set} 32    \033[38;5;97m {set} 97    \033[38;5;162m {set} 162    \033[38;5;227m {set} 227
    \033[38;5;33m {set} 33    \033[38;5;98m {set} 98    \033[38;5;163m {set} 163    \033[38;5;228m {set} 228
    \033[38;5;34m {set} 34    \033[38;5;99m {set} 99    \033[38;5;164m {set} 164    \033[38;5;229m {set} 229
    \033[38;5;35m {set} 35    \033[38;5;100m {set} 100   \033[38;5;165m {set} 165    \033[38;5;230m {set} 230
    \033[38;5;36m {set} 36    \033[38;5;101m {set} 101   \033[38;5;166m {set} 166    \033[38;5;231m {set} 231
    \033[38;5;37m {set} 37    \033[38;5;102m {set} 102   \033[38;5;167m {set} 167    \033[38;5;232m {set} 232
    \033[38;5;38m {set} 38    \033[38;5;103m {set} 103   \033[38;5;168m {set} 168    \033[38;5;233m {set} 233
    \033[38;5;39m {set} 39    \033[38;5;104m {set} 104   \033[38;5;169m {set} 169    \033[38;5;234m {set} 234
    \033[38;5;40m {set} 40    \033[38;5;105m {set} 105   \033[38;5;170m {set} 170    \033[38;5;235m {set} 235
    \033[38;5;41m {set} 41    \033[38;5;106m {set} 106   \033[38;5;171m {set} 171    \033[38;5;236m {set} 236
    \033[38;5;42m {set} 42    \033[38;5;107m {set} 107   \033[38;5;172m {set} 172    \033[38;5;237m {set} 237
    \033[38;5;43m {set} 43    \033[38;5;108m {set} 108   \033[38;5;173m {set} 173    \033[38;5;238m {set} 238
    \033[38;5;44m {set} 44    \033[38;5;109m {set} 109   \033[38;5;174m {set} 174    \033[38;5;239m {set} 239
    \033[38;5;45m {set} 45    \033[38;5;110m {set} 110   \033[38;5;175m {set} 175    \033[38;5;240m {set} 240
    \033[38;5;46m {set} 46    \033[38;5;111m {set} 111   \033[38;5;176m {set} 176    \033[38;5;241m {set} 241
    \033[38;5;47m {set} 47    \033[38;5;112m {set} 112   \033[38;5;177m {set} 177    \033[38;5;242m {set} 242
    \033[38;5;48m {set} 48    \033[38;5;113m {set} 113   \033[38;5;178m {set} 178    \033[38;5;243m {set} 243
    \033[38;5;49m {set} 49    \033[38;5;114m {set} 114   \033[38;5;179m {set} 179    \033[38;5;244m {set} 244
    \033[38;5;50m {set} 50    \033[38;5;115m {set} 115   \033[38;5;180m {set} 180    \033[38;5;245m {set} 245
    \033[38;5;51m {set} 51    \033[38;5;116m {set} 116   \033[38;5;181m {set} 181    \033[38;5;246m {set} 246
    \033[38;5;52m {set} 52    \033[38;5;117m {set} 117   \033[38;5;182m {set} 182    \033[38;5;247m {set} 247
    \033[38;5;53m {set} 53    \033[38;5;118m {set} 118   \033[38;5;183m {set} 183    \033[38;5;248m {set} 248
    \033[38;5;54m {set} 54    \033[38;5;119m {set} 119   \033[38;5;184m {set} 184    \033[38;5;249m {set} 249
    \033[38;5;55m {set} 55    \033[38;5;120m {set} 120   \033[38;5;185m {set} 185    \033[38;5;250m {set} 250
    \033[38;5;56m {set} 56    \033[38;5;121m {set} 121   \033[38;5;186m {set} 186    \033[38;5;251m {set} 251
    \033[38;5;57m {set} 57    \033[38;5;122m {set} 122   \033[38;5;187m {set} 187    \033[38;5;252m {set} 252
    \033[38;5;58m {set} 58    \033[38;5;123m {set} 123   \033[38;5;188m {set} 188    \033[38;5;253m {set} 253
    \033[38;5;59m {set} 59    \033[38;5;124m {set} 124   \033[38;5;189m {set} 189    \033[38;5;254m {set} 254
    \033[38;5;60m {set} 60    \033[38;5;125m {set} 125   \033[38;5;190m {set} 190    \033[38;5;255m {set} 255
    \033[38;5;61m {set} 61    \033[38;5;126m {set} 126   \033[38;5;191m {set} 191
    \033[38;5;62m {set} 62    \033[38;5;127m {set} 127   \033[38;5;192m {set} 192
    \033[38;5;63m {set} 63    \033[38;5;128m {set} 128   \033[38;5;193m {set} 193
    \033[38;5;64m {set} 64    \033[38;5;129m {set} 129   \033[38;5;194m {set} 194
    '''

def rainbow_gradient(word):
    from math import ceil
    txt = f'{word}'
    light_red = '\033[1;91m'
    light_yellow = '\033[1;93m'
    light_green = '\033[1;92m'
    light_blue = '\033[1;94m'
    light_cyan = '\033[1;96m'
    light_purple = '\033[1;95m'

    dic_color = [
        light_red, light_yellow, light_green, light_blue, light_cyan, light_purple, light_red, light_yellow,
        light_green, light_blue, light_cyan, light_purple, light_red, light_yellow, light_green, light_blue, light_cyan,
        light_purple, light_red, light_yellow, light_green, light_blue, light_cyan, light_purple, light_red,
        light_yellow, light_green, light_blue, light_cyan, light_purple, light_red, light_yellow, light_green,
        light_blue, light_cyan, light_purple, light_red, light_yellow, light_green, light_blue, light_cyan,
        light_purple, light_red, light_yellow, light_green, light_blue, light_cyan, light_purple, light_red,
        light_yellow, light_green, light_blue, light_cyan, light_purple, light_red, light_yellow, light_green,
        light_blue, light_cyan, light_purple, light_red, light_yellow, light_green, light_blue, light_cyan,
        light_purple, light_red, light_yellow, light_green, light_blue, light_cyan, light_purple
    ]
    txt2 = (r'''                                                                                             
    `7MMM.     ,MMF'`7MMF'`7MM"""Yb.   `7MN.   `7MF'`7MMF'  .g8"""bgd  `7MMF'  `7MMF'MMP""MM""YMM 
      MMMb    dPMM    MM    MM    `Yb.   MMN.    M    MM  .dP'     `M    MM      MM  P'   MM   `7 
      M YM   ,M MM    MM    MM     `Mb   M YMb   M    MM  dM'       `    MM      MM       MM      
      M  Mb  M' MM    MM    MM      MM   M  `MN. M    MM  MM             MMmmmmmmMM       MM      
      M  YM.P'  MM    MM    MM     ,MP   M   `MM.M    MM  MM.    `7MMF'  MM      MM       MM      
      M  `YM'   MM    MM    MM    ,dP'   M     YMM    MM  `Mb.     MM    MM      MM       MM      
    .JML. `'  .JMML..JMML..JMMmmmdP'   .JML.    YM  .JMML.  `"bmmmdPY  .JMML.  .JMML.   .JMML.                                                                                     
    ''').strip()

    split = txt.split(None, 16)  # Tudo
    split_line = txt.split('\n')
    num_lines = len(split_line)  # Numero de \n

    process_number = 0
    count = -1

    for c in range(num_lines):
        # PEGAR A 1 LINHA
        line1 = split_line[process_number]  # Linha 1

        # DIVIDIR 1 LINHA POR 12
        num_line1 = len(line1)  # Num de caracteres da 1 linha
        num_line1_12 = ceil(num_line1 / 16)  # Num de caracteres da 1 linha / 12

        # CRIAR LISTA COM A 1 LINHA CORTADA DE 12 EM 12
        replace_order = 1
        replace_order_1 = 0

        plus_fim = num_line1_12
        plus_inicio = 0
        list12 = []
        for c in range(16):
            list12.append(line1[plus_inicio:plus_fim])
            plus_fim += num_line1_12
            plus_inicio += num_line1_12


        # DEGRADE DA 1 LINHA
        list12_count = 0
        color = 'mid.vrc'
        count += 1
        for c in range(16):
            color = dic_color[count]
            count += 1
            # print('\n{:{}}'.format(f'{color}■'*div_line, num_line), end='')
            print(f'{color}{list12[list12_count]}', end='')
            list12_count += 1
        process_number += 1
        count -= 16

        return ''
    # FAZER TODO O PROCESSO PARA AS OUTRAS LINHAS

