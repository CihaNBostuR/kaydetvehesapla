from django.db import models

class CheckboxData(models.Model):
    data = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    selected_options = models.IntegerField(default=0)
    fee = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    
    

