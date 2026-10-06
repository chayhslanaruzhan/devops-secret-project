# DevOps Secret Project

## Жоба сипаттамасы
Бұл жоба CI/CD жүйесінде құпия деректерді қауіпсіз сақтауды көрсету үшін жасалды.

## Нұсқа
46-нұсқа — CI/CD жүйесінде secrets қауіпсіз сақтауды баптау.

## Қолданылған технологиялар
- GitHub
- GitHub Actions
- Python
- pytest
- GitHub Secrets

## Жобаның жұмысы
Қосымша APP_SECRET атты құпия мәннің бар-жоғын тексереді.
Құпия мән код ішінде сақталмайды және GitHub Secrets арқылы беріледі.

## CI/CD кезеңдері
1. Repository checkout
2. Python ортасын дайындау
3. pytest орнату
4. Build check
5. Test
6. Secret-ті қауіпсіз тексеру

## Тестілеу
Жобада екі автоматты тест бар:
- secret бар кезде тексеру;
- secret жоқ кезде тексеру.

## Нәтиже
Build — SUCCESS  
Test — SUCCESS  
Pipeline — SUCCESS
