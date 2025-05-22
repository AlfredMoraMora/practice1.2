from Robot import Robot
from Tache import Tache
import random
import jsonpickle


class Jeu:
    """
    Classe représentant le jeu où les joueurs achètent des robots et tentent d'accomplir des tâches.
    """
    def __init__(self, argent_depart: int, lst_robots:list[Robot]=[]) -> None:
        self.argent: int = argent_depart
        self.lst_robots = lst_robots
        # TODO : Charger la liste de robots à partir du fichier robots.json au lieu de créer les instances une par une. (env. 5 min)

        with open("robots.json", "r", encoding="utf-8") as fichier:
            objet_encode = fichier.read()
        self.lst_robots = jsonpickle.decode(objet_encode)
        # robots = []
        # for robot in self.lst_robots:     # Je ne sais pas comment le faire.. .
        #     robots = Robot(robot)


        # self.robots: list[Robot] = [
        #     Robot("Titan", 100, 8, 3, 2),
        #     Robot("Bolt", 120, 5, 7, 3),
        #     Robot("Neuro", 90, 3, 4, 9),
        #     Robot("Goliath", 150, 10, 2, 1),
        #     Robot("Rapide", 110, 4, 9, 4),
        #     Robot("Cerveau", 130, 2, 3, 10),
        #     Robot("Broyeur", 140, 9, 5, 2),
        #     Robot("Coureur", 105, 3, 10, 3),
        #     Robot("Lourd", 125, 7, 2, 6),
        #     Robot("Optimus", 160, 6, 6, 6)
        # ]
        self.taches: list[Tache] = [
            Tache("Course", 2, 10, 2, 100),
            Tache("Construction", 8, 3, 4, 120),
            Tache("Combat", 10, 2, 2, 150),
            Tache("Exploration", 4, 5, 8, 130),
            Tache("Dépannage", 3, 3, 10, 110)
        ]
        self.taches_selectionnees: list[Tache] = random.sample(self.taches, 3)
        self.equipe: list[Robot] = []

    def acheter_robot(self, robot: Robot) -> None:
        """
        Ajoute le robot à l'équipe si l'argent est suffisant.
        Un message de réussite ou d'échec est affiché.
        L'argent est déduit.

        :param robot: Le robot à acheter.
        """
        # TODO : Compléter la méthode (env. 10 min)
        pass


    def tenter_tache(self, tache: Tache) -> bool:
        """
        Tente d'accomplir une tâche avec l'équipe actuelle de robots.
        Un message de réussite ou d'échec est affiché.
        La tâche est réussie si les statistiques cumulées de l'équipe remplissent les exigences de la tâche.
        Une tâche réussie rapporte de l'argent.

        :param tache: La tache actuelle à accomplir.
        :return: True si la tache est réussie, False sinon.

        """
        # TODO : Compléter la méthode (env. 30 min)
        pass

    def jouer(self) -> None:
        """
        Démarre le jeu, permet d'acheter des robots et de tenter des tâches.
        """
        print(f"Bienvenue dans le jeu! Vous commencez avec {self.argent} crédits.")
        print("\nRobots disponibles à l'achat : ")
        for i, robot in enumerate(self.robots, 1):
            print(f"{i}. {robot}")
        print("\nTâches à accomplir:")
        for tache in self.taches_selectionnees:
            print(tache)

        while len(self.equipe) < 5 and self.argent >= min(robot.cout for robot in self.robots):
            choix = int(input("Choisissez un robot à acheter (1-10) ou 0 pour terminer l'achat: "))
            if choix == 0:
                break
            elif 1 <= choix <= 10:
                self.acheter_robot(self.robots[choix - 1])
            else:
                print("Choix invalide.")

        print("\nDébut des tâches:")
        accomplies = 0
        for tache in self.taches_selectionnees:
            if self.tenter_tache(tache):
                accomplies += 1

        if accomplies >= 3:
            # TODO : Lorsqu'une personne gagne, lui demander son pseudo et l'inscrire dans un fichier highscores.txt
            #        avec le montant d'argent restant ansi que la date et l'heure de la victoire (env. 5 min)
            print(f"Félicitations! Vous avez gagné avec {self.argent} crédits restants!")
        else:
            print("Vous avez perdu ! Il vaut mieux revoir votre stratégie.")




if __name__ == "__main__":


    jeu = Jeu(argent_depart=300)
    # jeu.jouer()
    print(jeu.load_robots())