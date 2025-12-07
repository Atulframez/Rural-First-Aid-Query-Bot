# Rural First Aid Query Bot

def emergency_numbers():
    print("\n EMERGENCY NUMBERS IN INDIA:")
    print(" Ambulance: 108")
    print(" Police: 100")
    print(" Fire Services: 101")
    print(" Women Helpline: 1091")
    print(" Child Helpline: 1098")
    print(" All-in-one Emergency: 112")
    print(" Poison Helpline (AIIMS): 1800-116-117\n")


def show_welcome():
    print("-----------------------------------------------------")
    print("            RURAL FIRST AID QUERY BOT              ")
    print("-----------------------------------------------------")
    print("Get basic first-aid help instantly during emergencies.\n")
    print("⚠ This is NOT a substitute for a doctor or hospital.")
    print("   Always contact medical help when available.\n")


def show_menu():
    print("\nSelect the emergency type:")
    print("1. Snakebite")
    print("2. Burn")
    print("3. Fracture")
    print("4. Fainting / Unconsciousness")
    print("5. Heavy bleeding")
    print("6. Nosebleed")
    print("7. Heart attack signs")
    print("8. Heat stroke / Sunstroke")
    print("9. Electric shock")
    print("10. Choking")
    print("11. Animal bite (dog/monkey)")
    print("12. General first-aid tips")
    print("13. Pregnancy emergency & childbirth kit")
    print("14. Emergency phone numbers")
    print("15. Exit\n")


# ------------------ CODE: Atul Anand & Bhavya Chauhan ------------------ #

def snakebite():
    print("\n Snakebite First Aid:")
    print("- Keep patient calm + reduce movement (slows venom spread).")
    print("- Keep bite area lower than heart level.")
    print("- Remove tight clothing/jewellery near swelling.")
    print("- Take to hospital immediately.")
    print(" Do NOT cut wound / suck venom / apply ice / tight band.\n")

def burn():
    print("\n Burn First Aid:")
    print("- Wash area under cool running water for 15+ mins.")
    print("- Cover with clean cloth/sterile gauze.")
    print("- For blisters, don't break them.")
    print(" Do NOT apply toothpaste, ghee, oil, turmeric etc.\n")

def fracture():
    print("\n Fracture First Aid:")
    print("- Immobilize area, avoid movement.")
    print("- Make a temporary splint with wood/cardboard + cloth.")
    print("- Apply cold compress outside cloth.")
    print(" Do NOT try to set broken bone yourself.\n")

def fainting():
    print("\n Fainting / Unconscious:")
    print("- Lay person on back, lift legs slightly.")
    print("- Ensure airflow, loosen clothes.")
    print("- If vomiting, turn to side.")
    print(" Never give water/food until fully conscious.\n")

def bleeding():
    print("\n Heavy Bleeding:")
    print("- Apply firm pressure with clean cloth/bandage.")
    print("- Elevate wound above heart if possible.")
    print("- Add cloth layers, do NOT remove soaked ones.")
    print(" Avoid very tight tourniquets unless trained.\n")

def nosebleed():
    print("\n Nosebleed:")
    print("- Sit and lean forward slightly.")
    print("- Pinch nose soft part 10–15 mins.")
    print("- Put cold compress on nose/neck.")
    print(" Do NOT tilt head back (blood may go into throat).\n")

def heart_attack():
    print("\n Possible Heart Attack Warning Signs:")
    print("- Chest pain/pressure spreading to arm/jaw.")
    print("- Sweating, breathlessness, nausea, dizziness.")
    print("- Help patient sit & stay calm.")
    print("- Chew 1 adult aspirin if not allergic + ambulance immediately.")
    print(" Don't leave person alone.\n")

def heat_stroke():
    print("\n Heat Stroke / Sunstroke:")
    print("- Move to shade, loosen clothes, cool with water.")
    print("- Give ORS / water small sips if conscious.")
    print("- Use wet cloth on body to cool.")
    print(" Do NOT give cold bath suddenly.\n")

def electric_shock():
    print("\n Electric Shock:")
    print("- FIRST: Turn off power source before touching victim.")
    print("- Check breathing & pulse; start CPR if trained.")
    print("- Treat burns with cool water.")
    print(" Never touch victim with bare hands if power ON.\n")

def choking():
    print("\n Choking First Aid:")
    print("- Encourage coughing first.")
    print("- If severe: perform 5 back blows + 5 abdominal thrusts (if trained).")
    print("- For child: gentle back blows only.")
    print(" Never put fingers inside throat blindly.\n")

def animal_bite():
    print("\n Dog/Monkey Bite:")
    print("- Wash wound with soap/water for 15 mins.")
    print("- Apply antiseptic.")
    print("- Visit hospital for anti-rabies shots immediately.")
    print(" Avoid tying wound tightly.\n")

def tips():
    print("\n General First Aid Tips:")
    print("- Keep first aid kit at home.")
    print("- Learn CPR officially if possible.")
    print("- Check emergency numbers in your area.\n")


# --------- CODE : Bhavya Chauhan  --------- #

def pregnancy_emergency():
    print("\n Pregnancy Emergency / Childbirth Kit (when hospital is far):\n")
    print(" Signs labour may have started:")
    print("- Regular strong contractions")
    print("- Water breaking (fluid discharge)")
    print("- Continuous lower back/abdominal pain\n")

    print(" If delivery seems close:")
    print("- Keep mother calm and lay her on a clean, flat surface.")
    print("- Wash hands thoroughly with soap or use sanitizer.")
    print("- Place a clean cloth or towel under her.\n")

    print(" Emergency childbirth kit items:")
    print("- Soap / sanitizer")
    print("- Clean cloths / towels")
    print("- Sterile blade or scissors")
    print("- New, clean thread to tie umbilical cord")
    print("- Warm cloth/blanket for the baby\n")

    print(" After the baby is born (if before reaching hospital):")
    print("- Gently wipe baby’s mouth and nose to clear fluid.")
    print("- Keep baby warm, preferably skin-to-skin with mother.")
    print("- When cord stops pulsating: tie two knots with thread and cut between them with sterile blade.")
    print("- Do NOT pull the placenta; let it come out naturally.\n")

    print(" Go to a hospital urgently if:")
    print("- Heavy bleeding continues")
    print("- Baby is not crying/breathing properly")
    print("- Very long labour with no progress")
    print("- Mother has convulsions or severe pain\n")

    print("⚠ This guidance is only for emergency delay situations.")
    print("   Medical assistance is always essential.\n")


# ------------------ MAIN CODE : Atul Anand ------------------ #

def main():
    show_welcome()

    while True:
        show_menu()
        c = input("Enter your choice (1-15): ").strip()

        options = {
            "1": snakebite,
            "2": burn,
            "3": fracture,
            "4": fainting,
            "5": bleeding,
            "6": nosebleed,
            "7": heart_attack,
            "8": heat_stroke,
            "9": electric_shock,
            "10": choking,
            "11": animal_bite,
            "12": tips,
            "13": pregnancy_emergency,
            "14": emergency_numbers
        }

        if c in options:
            options[c]()
        elif c == "15":
            print("\nThank you for using Rural First Aid Query Bot!")
            print("Stay alert, stay safe. ")
            break
        else:
            print("Invalid input, try again.\n")


if __name__ == "__main__":
    main()