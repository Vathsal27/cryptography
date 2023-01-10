from django.shortcuts import render, redirect
from django.contrib import messages
from .functions import *


def cryptography(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            input = request.POST.get('input')
            shift = request.POST.get('shift')
            if ("submit" in request.POST):      # button condition
                output = ""
                if (request.POST.get("function") == "option1"):
                    output = text_to_morse(input)

                elif (request.POST.get("function") == "option2"):
                    output = morse_to_text(input)

                elif (request.POST.get("function") == "option3"):
                    output = camel_to_snake(input)

                elif (request.POST.get("function") == "option4"):
                    output = inverseCase(input)

                elif (request.POST.get("function") == "option5"):
                    if request.POST['shift']:
                        int_shift = int(shift)
                        output = caesar_cipher(input, int_shift)
                    else:
                        messages.error(request,"Shift/Key field found empty!")
                        return redirect("cryptography")

                elif (request.POST.get("function") == "option6"):
                    if request.POST['shift']:
                        output = vigenere_cipher(input, shift) 
                    else:
                        messages.error(request,"Shift/Key field found empty!")
                        return redirect("cryptography")

                elif (request.POST.get("function") == "option7"):
                    output = base64_en(input)

                elif (request.POST.get("function") == "option8"):
                    output = base64_de(input)

                elif (request.POST.get("function") == "option9"):
                    if request.POST['shift']:
                        int_shift = int(shift)
                        output = caesar_decipher(input, int_shift)
                    else:
                        messages.error(request,"Shift/Key field found empty!")
                        return redirect("cryptography")

                elif (request.POST.get("function") == "option10"):
                    if request.POST['shift']:
                        output = vigenere_decipher(input, shift)
                    else:
                        messages.error(request,"Shift/Key field found empty!")
                        return redirect("cryptography")

                elif (request.POST.get("function") == "option11"):
                    output = snake_to_camel(input)

                return render(request, 'crypto_functions/cryptography.html', {'output':output})
    else:
        return redirect("login")
    return render(request, 'crypto_functions/cryptography.html')