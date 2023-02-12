from django.shortcuts import render
from django.http import HttpResponse
from .forms import FileForm
from .models import Upload,Cnab


def store_file(request):
   if request.method == 'POST':
      form = FileForm(request.POST, request.FILES)
      file = request.FILES['file']

      cnab_file = Upload.objects.create(cnab_file=file)
      cnab_file.save()

      list_files = []

      with open(f"uploads/{str(cnab_file.cnab_file)}", "r", encoding="utf-8") as read_file:
         for file_line in read_file:
            list_files.append(file_line)

      for line in list_files:
         tipo    = line[:1]
         ano     = line[1:5]
         mes     = line[5:7]
         dia     = line[7:9]
         valor   = line[9:19]
         cpf     = line[19:30]
         cartao  = line[30:42]
         hora    = line[42:44]
         minuto  = line[44:46]
         segundo = line[46:48]
         dono    = line[48:62]
         loja    = line[62:81]    

         data    = f"{dia}/{mes}/{ano}"
         valor   = int(valor)/100
         hora    =f"{hora}:{minuto}:{segundo}"

         if tipo == "1":
            tipo = "Débito"

         elif tipo == "2":
            tipo = "Boleto"

         elif tipo == "3":
            tipo = "Financiamento"

         elif tipo == "4":
            tipo = "Crédito"

         elif tipo == "5":
            tipo = "Empréstimo"

         elif tipo == "6":
            tipo = "Vendas"

         elif tipo == "7":
            tipo = "TED"

         elif tipo == "8":
            tipo = "DOC"

         elif tipo == "9":
            tipo = "Aluguel"
        

         result = Cnab.objects.create( tipo=tipo, data=data, valor=valor, cpf=cpf, cartao=cartao, hora=hora, dono=dono, loja=loja)
         result.save()

         transations = Cnab.objects.values("tipo", "valor", "data", "cpf", "hora", "dono", "loja")

         final_value = 0

      for transation in transations:
         if transation["tipo"] == "Aluguel" or transation["tipo"] == "Boleto" or transation["tipo"] == "Financiamento" :
            final_value -= transation["valor"]
         else:
            final_value += transation["valor"]

      return render(request, "results.html", context={"transations": transations, "final_value": final_value})
    
   else:

      form = FileForm()
   return render(request, "upload_file.html", {"form": form})