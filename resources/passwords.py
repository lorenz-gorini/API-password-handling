from flask_restful import Resource
import enchant

class Password(Resource):
    def get(self, psw:str, complexity:int):
        complexity_dict = {1:"weak", 2:"medium", 3:"strong"}
        # The two variables may be wrong
        if not (complexity in complexity_dict.keys()):
            return {
                    "message":f"The complexity index {complexity} was not a permitted value: {complexity_dict.keys()}"
                   }, 400

        if psw == "":
            return {
                    "message":f"The password field is empty"
                   }, 400


        # Now it checks the password according to the complexity level required
        capital_letters, digits, lowercase_letters, special_char = 0, 0, 0, 0
        numbers = set([str(s) for s in range(10)])
        spec_symb = {"$","#","@","_","-"}
        # This is needed to keep the psw value
        psw_to_letter = psw
        for psw_char in psw:
            if psw_char in numbers: digits += 1
            elif psw_char in spec_symb:
                special_char += 1
                # 1. Take off the special characters in order to verify if the resulting password is a dictionary word
                psw_to_letter = psw_to_letter.replace(psw_char,"")
            elif psw_char.upper() == psw_char: capital_letters +=1
            elif psw_char.lower() == psw_char: lowercase_letters += 1


        # Check if the password corresponds to a single dictionary word
        # 1: [we have done it above]
        # 2: replace numbers with possible letters
        num_to_lett_dict = {"1":"i","2":"z","3":"e","4":"l","5":"s","6":"b","7":"f","8":"b","9":"g","0":"o"}
        for l in num_to_lett_dict.keys():
            psw_to_letter = psw_to_letter.replace(l,num_to_lett_dict[l])
        # Check in the english dictionary
        enchant_dict = enchant.Dict("en_US")
        is_in_dictionary = enchant_dict.check(psw_to_letter.lower())

        # Generate the resulting messages
        ok_message = {
                            "message":f"{complexity_dict[complexity].upper()}  as you required. Great Password!"
                     }, 200
        non_compliant_mess = {
                                    "message":f"NOT {complexity_dict[complexity].upper()}  as you required. "
                                              f"Sorry but you need to try another one. Check the constraints below!"
                             }, 200

        # According to the selected complexity, we check if the password complies to the required constraints
        if lowercase_letters != 0 and digits != 0 and len(psw)<15:
            if complexity == 1:
                return ok_message
            elif capital_letters != 0 and special_char != 0 and len(psw)>= 5:
                if complexity == 2:
                    return ok_message
                elif not is_in_dictionary:
                    return ok_message
                else:
                    # The required complexity = 3, but the password fulfills only the level 2 constraints
                    return non_compliant_mess
            else:
                # The required complexity >= 2, but the password fulfills only the level 1 constraints
                return non_compliant_mess
        else:
            return { "message": "not even WEAK. Sorry but you need to try another one." }, 200


if __name__ == "__main__":
    instan = Password().get("L0w3r#","3")
    print(instan)