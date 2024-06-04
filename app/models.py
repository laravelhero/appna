from django.db import models

class Member(models.Model):
    PREFIX = {
        "DR": "Dr.",
        "MR": "Mr."
    }
    STATE = {
        "TX": "Texas",
    }
    COUNTRY = {
        "US": "United States",
    }
    MEDICAL = {
        "DMC": "Dow Medical College",
        "SMC": "Sindh Medical College",
        "AKMC": "Aga Khan Medical College",
        "BMC": "Baqai Medical College",
        "KMDC": "Karachi Medical and Dental College",
        "ZMC": "Ziauddin Medical College",
        "JMC": "Jamshoro Medical College",
        "KEMC": "King Edward Medical College",
        "AIMC": "Allama Iqbal Medical College",
        "FJMC": "Fatima Jinnah Medical College",
        "RMC": "Rawalpindi Medical College",
        "NMC": "Nishtar Medical College",
        "AMC": "Ayub Medical College",
        "BMC": "Bolan Medical College",
        "Others": "Others",
    }
    MEMBERSHIP_TYPE = {
        100: "Lifetime Member ($100)",
    }
    prefix = models.CharField(max_length=2, choices=PREFIX, default=PREFIX['DR'])
    full_name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=30, null=True)
    phone = models.CharField(max_length=15, null=True)
    home_phone = models.CharField(max_length=15, blank=True, null=True)
    office_phone = models.CharField(max_length=15, blank=True, null=True)
    location = models.CharField(max_length=50, null=True)
    other_location = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=15, blank=True, null=True)
    state = models.CharField(max_length=20, choices=STATE, default=STATE['TX'])
    zip_code = models.CharField(max_length=15, blank=True, null=True)
    country = models.CharField(max_length=20, choices=COUNTRY, default=COUNTRY['US'])
    medical = models.CharField(max_length=20, choices=MEDICAL, null=True)
    year_of_graduation = models.CharField(max_length=15, null=True)
    membership_type = models.CharField(max_length=20, choices=MEMBERSHIP_TYPE, default=MEMBERSHIP_TYPE[100])
    profile_photo = models.ImageField(default='profile-pic.jpg', upload_to='member', blank=True, null=True)
    license = models.ImageField(blank=True,upload_to='member/license', null=True)

    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = "1. Member List"
    
class Donation(models.Model):
    full_name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=30, null=True)
    phone = models.CharField(max_length=30, null=True)     
    purpose = models.CharField(max_length=100, null=True)
    amount = models.IntegerField()
    
    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = "2. Donor List"