from django.contrib import admin
from .models import DataForm
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.utils import ImageReader
from django.http import HttpResponse

class DataFormAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'pnf', 'semestre', 'cedula', 'created_at')
    
    actions = ['generate_pdf']
    
    def generate_pdf(self, request, queryset):
        dataform_id = queryset.values_list('id', flat=True)[0]
        
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = ' attachment ; filename="constancia.pdf" '
        
        p = canvas.Canvas(response, pagesize=letter)
        
        margen = inch
        ancho, alto = letter
        
        dataform = DataForm.objects.get(id=dataform_id)
        nombres = dataform.nombres
        apellidos = dataform.apellidos
        edad = dataform.edad
        pnf = dataform.pnf
        seccion = dataform.seccion
        semestre = dataform.semestre
        cedula = dataform.cedula
        fecha = dataform.created_at
        
        
        p.setTitle(f"Constancia de estudio {nombres}")
        p.setFont('Times-Roman',12)
        
        imagen = ImageReader("solicitud/static/images/Logo_Unexca.jpg")
        p.drawImage(imagen, 50, 730, width=50, height=50)
        texto = f"""REPUBLICA BOLIVARIANA DE VENEZUELA <br/>
                    MINISTERIO DEL PODER POPULAR PARA LA EDUCACION UNIVERSITARIA <br/>
                    UNIVERSIDAD NACIONAL EXPERIMENTAL DE LA GRAN CARACAS - UNEXCA"""
        
        estilo = ParagraphStyle(name="Normal", alignment=1, spaceBefore=0, spaceAfter=0, leading=18)
        
        parrafo = Paragraph(texto,estilo)
        
        parrafo.wrapOn(p, ancho - 2 * margen, alto - 2 * margen)
        parrafo.drawOn(p, margen, margen * 10)
        
        p.drawCentredString(ancho / 2, alto - 2 * margen, "CONSTANCIA DE ESTUDIOS")
        
        texto2 = f"""Quien suscribe, Ing. Yovany Diaz, Jefe(E) Coordinacion Control de Estudios de la UNIVERSIDAD NACIONAL EXPERIMENTAL
        DE LA GRAN CARACAS, hace constar por medio la presente que el(la) ciudadano(na) {apellidos} {nombres}, titular de la cedula de identidad
        Nº {cedula}, es estudiante activo(a) de esta universidad en el nucleo Altagracia actualmente cursa periodo academico 00/00/2023
        al 00/00/2024. del Programa Nacional de Formacion Informatica, seccion {seccion}, turno Matutino. <br/> <br/>
        
        Constancia que se expide a peticion de la parte interesada en Caracas, {fecha}"""
        
        estilo2 = ParagraphStyle(name="Normal", alignment=4, spaceBefore=0, spaceAfter=0, leading=18)
        parrafo2 = Paragraph(texto2, estilo2)
        
        parrafo2.wrapOn(p, ancho - 2 * margen, alto - 2 * margen)
        parrafo2.drawOn(p, margen, margen * 6)
        
        texto3 = f"""Atentamente, <br/> <br/> <br/>
                    ING YOVANY DIAZ <br/>
                    JEFE(E) COORDINACION CONTROL DE ESTUDIOS  <br/>
                    NUCLEO-ALTAGRACIA"""
        
        ancho2 = 8.5 * inch
        x1 = 50
        x2 = 250
        y = 270
        ancho_linea = x2 - x1
        x = (ancho2 - ancho_linea) / 2
        p.line(x, y, x + ancho_linea, y)
        
        estilo3 = ParagraphStyle(name="Normal", alignment=1, spaceBefore=0, spaceAfter=0, leading=18)
        
        parrafo3 = Paragraph(texto3,estilo3)
        
        parrafo3.wrapOn(p, ancho - 2 * margen, alto - 2 * margen)
        parrafo3.drawOn(p, margen, margen * 3)
        
        p.showPage()
        p.save()
        return response
    generate_pdf.short_description = "Descarga los items como PDF"



# Register your models here.

admin.site.register(DataForm, DataFormAdmin)
