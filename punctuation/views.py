from django.http import HttpResponse
from django.shortcuts import render
  
  
def health(request):
    return HttpResponse("Its is Working!")   
 
def index(request):
    return render(request, 'index.html')

def remove_punctuations(request):
    text = request.GET.get('text', "NA")
    cap_tick = request.GET.get('capital', "No")
    tick = request.GET.get('Remove_Punctuation', "No")
    temp=""
    if tick == 'Yes':
        final_text=""
        for i in text:
            if i not in [",", ":", ".", ";","'",'''"''']:
                final_text = final_text + i
        temp = temp + "Punctuation"
    else:
        final_text = text
        
    if cap_tick == "Yes":
        final_text = capitalize(cap_tick ,final_text)
        if len(temp)!=0:
            temp= temp + " and capitalize"
        else:
            temp = temp + "capitalize"
    param ={"name": final_text, "out": temp}
    return render(request, 'punct.html', param)

def capitalize(tick,text):
    #tick = request.GET.get('capital', "No")
    #text = request.GET.get('text')
    if tick == "Yes":
        text = text.upper()
    return text
    