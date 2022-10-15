from django.shortcuts import render, redirect
from .models import *

from django.db.models import Q
from django.http import HttpResponse

from .tg import send_message_telegram
# Create your views here.
def home_page(request):
    phone = Phone.objects.first().phone_number
    darslar_soni = CourseName.objects.first().darslar_soni
    vazifalar_soni = CourseName.objects.first().vazifalar_soni
    kurs_nomi = CourseName.objects.first().name
    kurs_afzalliklari = CourseFacts.objects.all()
    teacher = Teacher.objects.first()
    teacher_facts = TeacherFacts.objects.all()
    kimlar_uchun = KimlarUchun.objects.all()

    learning_list_toq = LearningList.objects.filter(~Q(tartib_raqami=2))
    learning_list_juft = LearningList.objects.filter(~Q(tartib_raqami=1))

    loyihalar = Loyihalar.objects.first()
    loyihalar_facts = LoyihalarFacts.objects.all()

    feedbacks_toq = Feedbacks.objects.filter(~Q(tartib_raqami=2))
    feedbacks_juft = Feedbacks.objects.filter(~Q(tartib_raqami=1))

    sabab_title = SababTitle.objects.first()
    sabab_list = SababList.objects.all()

    qulayliklar = Qulayliklar.objects.all()

    kurs_afzal_footer = KursAfzalliklari.objects.all()

    imkoniyat = Imkoniyat.objects.first()

    if request.method == "POST":
        model = Ariza()
        model.name = request.POST['firstname']
        model.phone = request.POST['phone']
        model.telegram = request.POST['telegram']

        model.save()
        send_message_telegram(
            ism=request.POST['firstname'],
            telefon=request.POST['phone'],
            telegram=request.POST['telegram']
        )

        return redirect('success_page')


    ctx = {
        "phone": phone,
        "darslar_soni": darslar_soni,
        "vazifalar_soni": vazifalar_soni,
        "kurs_nomi": kurs_nomi,
        "kurs_afzalliklari": kurs_afzalliklari,
        "teacher": teacher,
        "teacher_facts": teacher_facts,
        "kimlar_uchun": kimlar_uchun,
        "learning_list_toq": learning_list_toq,
        "learning_list_juft": learning_list_juft,
        "loyihalar": loyihalar,
        "loyihalar_facts": loyihalar_facts,
        "feedbacks_toq": feedbacks_toq,
        "feedbacks_juft": feedbacks_juft,
        "sabab_title": sabab_title,
        "sabab_list": sabab_list,
        "qulayliklar": qulayliklar,
        "kurs_afzal_footer": kurs_afzal_footer,
        "imkoniyat": imkoniyat
    }
    return render(request, 'index.html', ctx)

def success_page(request):
    phone = Phone.objects.first().phone_number
    darslar_soni = CourseName.objects.first().darslar_soni
    vazifalar_soni = CourseName.objects.first().vazifalar_soni
    kurs_nomi = CourseName.objects.first().name
    kurs_afzalliklari = CourseFacts.objects.all()
    teacher = Teacher.objects.first()
    teacher_facts = TeacherFacts.objects.all()
    kimlar_uchun = KimlarUchun.objects.all()

    learning_list_toq = LearningList.objects.filter(~Q(tartib_raqami=2))
    learning_list_juft = LearningList.objects.filter(~Q(tartib_raqami=1))

    loyihalar = Loyihalar.objects.first()
    loyihalar_facts = LoyihalarFacts.objects.all()

    feedbacks_toq = Feedbacks.objects.filter(~Q(tartib_raqami=2))
    feedbacks_juft = Feedbacks.objects.filter(~Q(tartib_raqami=1))

    sabab_title = SababTitle.objects.first()
    sabab_list = SababList.objects.all()

    qulayliklar = Qulayliklar.objects.all()

    kurs_afzal_footer = KursAfzalliklari.objects.all()

    imkoniyat = Imkoniyat.objects.first()

    if request.method == "POST":
        print(request.POST)
        model = Ariza()
        model.name = request.POST['firstname']
        model.phone = request.POST['phone']
        model.telegram = request.POST['telegram']

        model.save()
        send_message_telegram(
            ism=request.POST['firstname'],
            telefon=request.POST['phone'],
            telegram=request.POST['telegram']
        )

        return redirect('success_page')


    ctx = {
        "phone": phone,
        "darslar_soni": darslar_soni,
        "vazifalar_soni": vazifalar_soni,
        "kurs_nomi": kurs_nomi,
        "kurs_afzalliklari": kurs_afzalliklari,
        "teacher": teacher,
        "teacher_facts": teacher_facts,
        "kimlar_uchun": kimlar_uchun,
        "learning_list_toq": learning_list_toq,
        "learning_list_juft": learning_list_juft,
        "loyihalar": loyihalar,
        "loyihalar_facts": loyihalar_facts,
        "feedbacks_toq": feedbacks_toq,
        "feedbacks_juft": feedbacks_juft,
        "sabab_title": sabab_title,
        "sabab_list": sabab_list,
        "qulayliklar": qulayliklar,
        "kurs_afzal_footer": kurs_afzal_footer,
        "imkoniyat": imkoniyat
    }
    return render(request, 'success.html', ctx)