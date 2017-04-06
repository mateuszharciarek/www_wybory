from django.shortcuts import render, render_to_response
import xlrd


def index(request):
    path = "dane/zal2.xls"
    book = xlrd.open_workbook(path)
    first_sheet = book.sheet_by_index(0)

    tmp = []
    wyniki = []
    ludzie = []
    razem = 0

    for i in range(3, 27):
        if i % 2 != 0:
            tmp.append(first_sheet.cell(6, i).value)
            razem += first_sheet.cell(6, i).value

    for i in range(3, 27):
        if i % 2 != 0:
            ludzie.append(first_sheet.cell(4, i).value)

    for i in tmp:
        wyniki.append(i / razem * 100)

    lista = []
    for i in range(3, 27):
        if i % 2 != 0:
            war = (first_sheet.cell(4, i), first_sheet.cell(6, i).value)
            lista.append(war)

    lista.sort(key=lambda tup: tup[1])
    return render_to_response('index.html', {'lista': lista})


def test(request):
    path = "dane/zal2.xls"
    book = xlrd.open_workbook(path)
    first_sheet = book.sheet_by_index(0)

    ludzie = []
    wyniki = []
    for i in range(3, 25):
        if i % 2 != 0:
            wyniki.append(first_sheet.cell(4, i).value)
    for i in range(3, 25):
        if i % 2 == 0:
            ludzie.append(first_sheet.cell(6, i).value)

    return render_to_response('template.html', {'wyniki': wyniki}, {'ludzie': ludzie})
