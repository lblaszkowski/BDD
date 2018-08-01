Feature: Tworzenie dokumentu

  Scenario Outline: Dodawanie nowego dokumentu zakonczone sukcesem
    Given Uzytkownik ma uruchomiony program
    And Tworzy nowy dokument
    When Uzytkownik wprowadza <ProjektID> i <DocumentID> oraz <DocumentName>
    And Zapisuje projekt
    Then Uzytkownik widzi  stworzony dokument o nazwie <NazwaDokumentu>

    Examples:
    | ProjektID | DocumentID | DocumentName | NazwaDokumentu |
    | 01      | Test         | Dokument     | 01-Test:|
