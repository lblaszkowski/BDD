Feature: Tworzenie dokumentu

  Scenario: Dodawanie nowego dokumentu zakonczone sukcesem
    Given Uzytkownik ma uruchomiony program
    And Tworzy nowy dokument
    When Uzytkownik wprowadza ProjektID i DocumentID oraz Document name
    And Zapisuje projekt
    Then Uzytkownik widzi  stworzony dokument o nazwie Nazwa
