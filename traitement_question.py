from constant import stop_words

class Question:
    """
    Classe permettant le parsing de la question
    """

    def traitement_question(user_question):
        """
        Méthode permettant de supprimer les stop_words de la question
        Retourne:
        user_question->question d'origine
        user_question_sw->question traitée
        """
        
        user_question1=user_question.split()
        user_question_sw=[element for element in user_question1 if element not in stop_words]
        user_question_sw=" ".join(user_question_sw)   
        return user_question_sw,user_question