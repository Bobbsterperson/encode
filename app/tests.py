import base64
import pytest
from django.urls import reverse
from .models import InputData

@pytest.mark.django_db
@pytest.mark.parametrize("input_text, expected_encoded", [
    ("hello", base64.b64encode(b"hello").decode('utf-8')),
    ("world", base64.b64encode(b"world").decode('utf-8')),
    ("Django", base64.b64encode(b"Django").decode('utf-8')),
])
def test_stuff_view(client, input_text, expected_encoded):
    response = client.post(reverse('submit'), {'topic': input_text})
    assert response.status_code == 200
    assert InputData.objects.filter(topic=input_text).exists()
    response_content = response.context['submitted_data']
    assert any(encoded == expected_encoded for _, encoded in response_content)
    assert any(original == input_text for original, _ in response_content)
