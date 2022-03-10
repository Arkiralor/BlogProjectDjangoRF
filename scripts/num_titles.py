from blogapp.models import Language

def main():
    languages = Language.objects.all()
    for lang in languages:
        print(f"Number of tiles in {lang.name}: {lang.num_of_titles}")

if __name__=="__main__":
    main()