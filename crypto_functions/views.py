from django.shortcuts import render, redirect
from django.contrib import messages
from .functions import *


def cryptography(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            input = request.POST.get('input')
            shift = request.POST.get('shift')
            if ("submit" in request.POST):      # button condition
                if (request.POST.get("function") == "opt1"):
                    output = text_to_morse(input)
                    return render(request, 'crypto_functions/cryptography.html', {'output':output})

                elif (request.POST.get("function") == "opt2"):
                    output = morse_to_text(input)
                    return render(request, 'crypto_functions/cryptography.html', {'output':output})

                elif (request.POST.get("function") == "opt3"):
                    output = camel_to_snake(input)
                    return render(request, 'crypto_functions/cryptography.html', {'output':output})

                elif (request.POST.get("function") == "opt4"):
                    output = inverseCase(input)
                    return render(request, 'crypto_functions/cryptography.html', {'output':output})

                elif (request.POST.get("function") == "opt5"):
                    if request.POST['shift']:
                        int_shift = int(shift)
                        output = caesar_cipher(input, int_shift)
                    else:
                        messages.error(request,"Shift/Key field found empty!")
                        return redirect("cryptography")
                    return render(request, 'crypto_functions/cryptography.html', {'output':output})

                elif (request.POST.get("function") == "opt6"):
                    if request.POST['shift']:
                        output = vigenere_cipher(input, shift) 
                    else:
                        messages.error(request,"Shift/Key field found empty!")
                        return redirect("cryptography")
                    return render(request, 'crypto_functions/cryptography.html', {'output':output})

                elif (request.POST.get("function") == "opt7"):
                    output = base64_en(input)
                    return render(request, 'crypto_functions/cryptography.html', {'output':output})

                elif (request.POST.get("function") == "opt8"):
                    output = base64_de(input)
                    return render(request, 'crypto_functions/cryptography.html', {'output':output})
    else:
        return redirect("login")
    return render(request, 'crypto_functions/cryptography.html')