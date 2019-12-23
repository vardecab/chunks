# TODO: what's that little thing here?

# encoder: https://ga-dev-tools.appspot.com/campaign-url-builder/
# to pre-fill URL: 
# https://docs.google.com/forms/d/1pyXtvJ-H4bcYQbAtviGof1CCTwgt-eWg0QYjx_hAfAQ/prefill
# pre-filled URL:
# https://docs.google.com/forms/d/e/1FAIpQLScDtDHdh6C-kUiNKOWRd_-SXvxwrZJUseYM4vAfkjSGaATTyA/viewform?usp=pp_url&
# entry.212735391=Tak,+ca%C5%82y+czas.
# &entry.1054984763=Nie
# &entry.673986204=Tak
# &entry.575141071=Zbyt+du%C5%BCy+%22luz%22.
# &entry.575141071=Brak+mo%C5%BCliwo%C5%9Bci+awansu.
# &entry.258987743=Oszcz%C4%99dno%C5%9B%C4%87+czasu+(np.+brak+konieczno%C5%9Bci+dojazdu,+szybsze+spotkania).
# &entry.258987743=Wi%C4%99ksza+swoboda.
# &entry.258987743=Wi%C4%99cej+wolnego+czasu.
# &entry.1460454061=Biuro
# &entry.53300176=Dom
# &entry.53300176=Przestrze%C5%84+co-workingowa
# &entry.2061846154=Marketing
# &entry.1190076232=M%C5%82odszy+specjalista+(junior)
# &entry.1635131053=6-20
# &entry.56442886=16-20

# = == === actual stuff when the fun begins 🚀 === == =
import random
import webbrowser 

print("Starting...")

# lists with questions and answers
entry_212735391 = ["Nie%2C+w+og%C3%B3le.", "Tak%2C+ale+nie+wi%C4%99cej+ni%C5%BC+1+dzie%C5%84+w+tygodniu.", "Tak%2C+wi%C4%99cej+ni%C5%BC+1+dzie%C5%84+w+tygodniu.", "Tak%2C+ca%C5%82y+czas."]
entry_1054984763 = ["Nie", "Tak"] # entry.1054984763
entry_673986204 = ["Nie", "Tak"] # entry.673986204
entry_575141071 = ["Brak+dedykowanej+przestrzeni+do+pracy.", "Zbyt+du%C5%BCy+%22luz%22.", "Wyd%C5%82u%C5%BCona+komunikacja+z+reszt%C4%85+zespo%C5%82u.", "Brak+mo%C5%BCliwo%C5%9Bci+nawi%C4%85zania+bli%C5%BCszych+relacji+ze+wsp%C3%B3%C5%82pracownikami.", "Ma%C5%82a+efektywno%C5%9B%C4%87.", "Brak+mo%C5%BCliwo%C5%9Bci+awansu.", "Brak+dost%C4%99pu+do+dokument%C3%B3w%2C+danych%2C+dokumentacji."]
entry_258987743 = ["Wi%C4%99ksza+swoboda.", "Wi%C4%99cej+wolnego+czasu.", "Brak+ci%C4%85g%C5%82ego+nadzoru+ze+strony+prze%C5%82o%C5%BConych.", "Oszcz%C4%99dno%C5%9B%C4%87+czasu+(np.+brak+konieczno%C5%9Bci+dojazdu%2C+szybsze+spotkania).", "Mo%C5%BCliwo%C5%9B%C4%87+lepszego+zaplanowania+dnia.", "Brak+zak%C5%82%C3%B3ce%C5%84%2C+nikt+i+nic+nie+przeszkadza+w+skupieniu+si%C4%99+nad+prac%C4%85."]
entry_1460454061 = ["Biuro", "Dom", "Przestrze%C5%84+co-workingowa", "Kawiarnia", "Park", "%C5%9Arodek+transportu+(np.+samoch%C3%B3d)", "Galeria+handlowa"]
entry_53300176 = ["Biuro", "Dom", "Przestrze%C5%84+co-workingowa", "Kawiarnia", "Park", "%C5%9Arodek+transportu+(np.+samoch%C3%B3d)", "Galeria+handlowa"]
entry_2061846154 = ["Marketing", "Us%C5%82ugi", "IT", "Finanse", "Budownictwo", "Transport", "Edukacja", "Medycyna"]
entry_1190076232 = ["M%C5%82odszy+specjalista+(junior)", "Sta%C5%BCysta+%2F+Asystent", "Specjalista", "Starszy+specjalista+(senior)", "Lider", "Mened%C5%BCer", "Dyrektor", "Zarz%C4%85d"]
entry_1635131053 = ["1", "2-5", "6-20", "21-50", "51-100", "101-200", "201-500", "500%2B"]
entry_56442886 = ["0%2B", "16-20", "21-25", "26-30", "31-40", "41-50"] 
entry_418804101 = [] # email address 

url_to_submit_without_answers = "https://docs.google.com/forms/d/e/1FAIpQLScDtDHdh6C-kUiNKOWRd_-SXvxwrZJUseYM4vAfkjSGaATTyA/formResponse?usp=pp_url"

loop_counter = 1 # always 1
how_many_runs = 69 # how many responses we want? 🤔
while loop_counter <= how_many_runs:
    
    print("Choosing answers...")

    url_to_submit = url_to_submit_without_answers + "&entry.212735391=" + random.choice(entry_212735391) + "&entry.1054984763=" + random.choice(entry_1054984763) + "&entry.673986204=" + random.choice(entry_673986204) + "&entry.575141071=" + random.choice(entry_575141071) + "&entry.575141071=" + random.choice(entry_575141071) + "&entry.258987743=" + random.choice(entry_258987743) + "&entry.258987743=" + random.choice(entry_258987743) + "&entry.1460454061=" + random.choice(entry_1460454061) + "&entry.53300176=" + random.choice(entry_53300176) + "&entry.53300176=" + random.choice(entry_53300176) + "&entry.2061846154=" + random.choice(entry_2061846154) + "&entry.1190076232=" + random.choice(entry_1190076232) + "&entry.1635131053=" + random.choice(entry_1635131053) + "&entry.56442886=" + random.choice(entry_56442886)

    # print (url_to_submit) # debug ✅

    print("Putting URL together...")

    webbrowser.open(url_to_submit, new=2, autoraise=False)
    print("Run:", loop_counter, "/", how_many_runs, "completed.")
    loop_counter += 1

print("Great success! :)")