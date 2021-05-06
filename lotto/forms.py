from django import forms
from .models import GuessNumbers

# Django에서 제공하는 ModelForm을 활용해 form 구성 모델 기반
class PostForm(forms.ModelForm):

    class Meta:
        model = GuessNumbers
        fields = ('name', 'text',) # 사용자로부터 form 통해 입력받을 데이터
