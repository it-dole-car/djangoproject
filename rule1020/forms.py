from socket import fromshare
from django.forms import ModelForm
from django.contrib.auth.forms import User
from .models import Barangay, Emp, Municipality
from django import forms

class User_login(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
class EmpForm(ModelForm):
    class Meta:
        model = Emp
        fields = '__all__'
        ordering= ['-updated','-created']
       
class CreateEmployer(forms.ModelForm):
    class Meta:
        model = Emp
        fields = '__all__'
    
    
    Eco_Activity=(
        ('-----------------------','-----------------------'),
        ('AGRICULTURE, FORESTRYAND FISHING','AGRICULTURE, FORESTRYAND FISHING'),
        ('MINING AND QUARRYING','MINING AND QUARRYING'),
        ('MANUFACTURING','MANUFACTURING'),
        ('WATER SUPPLY; SEWERAGE, WASTE MANAGEMENT AND REMEDIATION ACTIVITIES','WATER SUPPLY; SEWERAGE, WASTE MANAGEMENT AND REMEDIATION ACTIVITIES'),
        ('CONSTRUCTION','CONSTRUCTION'),
        ('WHOLESALE AND RETAIL TRADE; REPAIR OF MOTOR VEHICLES AND MOTORCYCLES','WHOLESALE AND RETAIL TRADE; REPAIR OF MOTOR VEHICLES AND MOTORCYCLES'),
        ('TRANSPORTATION AND STORAGE','TRANSPORTATION AND STORAGE'),
        ('ACCOMMODATION AND FOOD SERVICE ACTIVITIES','ACCOMMODATION AND FOOD SERVICE ACTIVITIES'),
        ('INFORMATION AND COMMUNICATION','INFORMATION AND COMMUNICATION'),
        ('FINANCIAL AND INSURANCE ACTIVITIES','FINANCIAL AND INSURANCE ACTIVITIES'),
        ('REAL ESTATE ACTIVITIES','REAL ESTATE ACTIVITIES'),
        ('PROFESSIONAL, SCIENTIFIC AND TECHNICAL ACTIVITIES','PROFESSIONAL, SCIENTIFIC AND TECHNICAL ACTIVITIES'),
        ('ADMINISTRATIVE AND SUPPORT SERVICE ACTIVITIES','ADMINISTRATIVE AND SUPPORT SERVICE ACTIVITIES'),
        ('PUBLIC ADMINISTRATION AND DEFENSE; COMPULSORY SOCIAL SECURITY','PUBLIC ADMINISTRATION AND DEFENSE; COMPULSORY SOCIAL SECURITY'),
        ('EDUCATION','EDUCATION'),
        ('HUMAN HEALTH AND SOCIAL WORK ACTIVITIES','HUMAN HEALTH AND SOCIAL WORK ACTIVITIES'),
        ('ARTS, ENTERTAINMENT AND RECREATION','ARTS, ENTERTAINMENT AND RECREATION'),
        ('OTHER SERVICE ACTIVITIES','OTHER SERVICE ACTIVITIES'),
        ('ACTIVITIES OF HOUSEHOLDS AS EMPLOYERS; UNDIFFERENTIATED GOODS-AND SERVICES-PRODUCING-ACTIVITIES OF HOUSEHOLDS FOR OWN USE','ACTIVITIES OF HOUSEHOLDS AS EMPLOYERS; UNDIFFERENTIATED GOODS-AND SERVICES-PRODUCING-ACTIVITIES OF HOUSEHOLDS FOR OWN USE'),
        ('ACTIVITIES OF EXTRATERRITORIAL ORGANIZATIONS AND BODIES','ACTIVITIES OF EXTRATERRITORIAL ORGANIZATIONS AND BODIES'),        
    )

    Legal_Org=(
        ('-----------------------','-----------------------'),
        ('Single Proprietorship','Single Proprietorship'),
        ('Partnership','Partnership'),
        ('Government Corporation','Government Corporation'),
        ('Private Corporation','Private Corporation'),
        ('Others','Others'),

    )

    Eco_Org=(
        ('-----------------------','-----------------------'),
        ('Single Establishment','Single Establishment'),
        ('Branch Only','Branch Only'),
        ('Establshment and main office','Establshment and main office'),
        ('Main Office only','Main Office only'),
        ('Ancillary unit (Except main office)','Ancillary unit (Except main office)'),

    )
    
    economic_organization = forms.ChoiceField(choices=Eco_Org)
    main_economic_activity= forms.ChoiceField(choices=Eco_Activity)
    legal_organization =forms.ChoiceField(choices=Legal_Org)
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['zip_code'].label = "PSGC"
        self.fields['building'].label = "Floor/Bldg No/Street/Subdivision"
        self.fields['labor_union'].label = "Name and Address of Labor Union, if any:"
      

        self.fields['municipality'].queryset = Municipality.objects.none()   
        if 'province' in self.data:
            try:
                province_id = int(self.data.get('province'))
                self.fields['municipality'].queryset = Municipality.objects.filter(province_id=province_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['municipality'].queryset = self.instance.province.municipality_set.order_by('name')

       
       
        self.fields['barangay'].queryset = Municipality.objects.none()
        if 'municipality' in self.data:
            try:
                municipality_id = int(self.data.get('municipality'))
                self.fields['barangay'].queryset = Barangay.objects.filter(municipality_id=municipality_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            #self.fields['vanue'].queryset = self.instance.country.city.vanue_set.order_by('name')
            self.fields['barangay'].queryset = self.instance.municipality.barangay_set.order_by('name')