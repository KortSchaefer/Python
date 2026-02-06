


crossword = [
    list("mfroslmdemonsandlunaydeyteicms"),
    list("tsocubasromuhriticatalgclthien"),
    list("ekieprecexperimentinsoapndedta"),
    list("vdicecahitedtoposvgslsmiteivht"),
    list("ieuerchaasngesktiecoeapywwiboa"),
    list("tvqcnodzcvypmritrihssvgbfoncdd"),
    list("aighacxzvyihpoaoecsktkloxhmwso"),
    list("ttklttledpaopeunytjncathoughts"),
    list("iaqrumiulprarstsunwptnostoahav"),
    list("trburftoawgcvipdzzsneahspgrcha"),
    list("nrsyasxunhgvfayklyeqzicwrnslwr"),
    list("aawjllojcynirocfcmzjpiogzhrxai"),
    list("unekbuiidpcaigahlldorstzcugzha"),
    list("qsseuidtcmpxisoxwukrambmwwjcgb"),
    list("lnnoxbzsalqvqlgjkbvlcnimjxrxyl"),
    list("kjrvnaxvbtfpoisrcilwtloxlabbfe"),
    list("agurqozbeligszefmtmjidjieybhms"),
    list("mcptlfwheyyvppefoqvychnssduton"),
    list("eqztvxlmvpzrepgjfpheemeiyabbnu"),
    list("tnviupdlhusrsduktpniarbwmnffgz"),
    list("hjtxneuropsychologyziakcacivql"),
    list("oiwatutauvccuztsjfivgachhndpvz"),
    list("dxcqwmkfxhnoxgonabviamosejtdjg"),
    list("toyewhydohrkulwqptgjkxhukkpqdc"),
    list("dugntleljhpziftphogiianrqpooxz"),
    list("npzpgvoqppzhizysjpseudovmqoxec"),
    list("uoazfgmcdjpaqfqdksegaexeavuzba"),
    list("wswsyonxpdamtfyflghaursynnzsxo"),
    list("tuktgdmfiotibrpfgywpxpasvuzazg"),
    list("yuoijpyxcxvzldukxdhggohkkhuixu"),
]

#vars
wordToFind = "exor"
WTFlist = list(wordToFind)


def Crossword():
    rows = len(crossword)
    cols = len(crossword[0]) if crossword else 0
    for row in range(rows):
        for coulmn in range(cols):
            if crossword[row][coulmn] == WTFlist[0]:
                # Use rows for vertical bounds and cols for horizontal bounds.
                # Also use len(wordToFind) - 1 to avoid off-by-one and negative indexing.
                if row <= rows - len(wordToFind):
                    VerticalCheckDown(row, coulmn)
                if row >= len(wordToFind) - 1:
                    VerticalCheckUp(row, coulmn)
                if coulmn <= cols - len(wordToFind):
                    HorazontalCheckRight(row, coulmn)
                if coulmn >= len(wordToFind) - 1:
                    HorazontalCheckLeft(row, coulmn)
                if row >= len(wordToFind) - 1 and coulmn <= cols - len(wordToFind):
                    DiagonalCheckNE(row, coulmn)
                if row <= rows - len(wordToFind) and coulmn <= cols - len(wordToFind):
                    DiagonalCheckSE(row, coulmn)
                if row >= len(wordToFind) - 1 and coulmn >= len(wordToFind) - 1:
                    DiagonalCheckNW(row, coulmn)
                if row <= rows - len(wordToFind) and coulmn >= len(wordToFind) - 1:
                    DiagonalCheckSW(row, coulmn)
def VerticalCheckUp(row, coulmn):
    guess1 = []
    for x in range(len(wordToFind)):
        # Up means decreasing row index
        guess1.append(crossword[row - x][coulmn])
    # Compare sequence, not sorted, to avoid anagram matches
    if guess1 == WTFlist:
        print(f'the first letter is in row {row}, coulmn {coulmn}')
def VerticalCheckDown(row, coulmn):
    guess1 = []
    for x in range(len(wordToFind)):
        # Down means increasing row index
        guess1.append(crossword[row + x][coulmn])
    if guess1 == WTFlist:
        print(f'the first letter is in row {row}, coulmn {coulmn}')

def HorazontalCheckRight(row, coulmn):
    guess1 = []
    for x in range(len(wordToFind)):
        guess1.append(crossword[row][coulmn+x])
    if guess1 == WTFlist:
        print(f'the first letter is in row {row}, coulmn {coulmn}')
def HorazontalCheckLeft(row, coulmn):
    guess1 = []
    for x in range(len(wordToFind)):
        guess1.append(crossword[row][coulmn-x])
    if guess1 == WTFlist:
        print(f'the first letter is in row {row}, coulmn {coulmn}')
def DiagonalCheckNE(row, coulmn):
    guess1 = []
    for x in range(len(wordToFind)):
        # North-East: row decreases, column increases
        guess1.append(crossword[row - x][coulmn + x])
    if guess1 == WTFlist:
        print(f'the first letter is in row {row}, coulmn {coulmn}')
def DiagonalCheckSE(row, coulmn):
    guess1 = []
    for x in range(len(wordToFind)):
        # South-East: row increases, column increases
        guess1.append(crossword[row + x][coulmn + x])
    if guess1 == WTFlist:
        print(f'the first letter is in row {row}, coulmn {coulmn}')
def DiagonalCheckSW(row, coulmn):
    guess1 = []
    for x in range(len(wordToFind)):
        # South-West: row increases, column decreases
        guess1.append(crossword[row + x][coulmn - x])
    if guess1 == WTFlist:
        print(f'the first letter is in row {row}, coulmn {coulmn}')
def DiagonalCheckNW(row, coulmn):
    guess1 = []
    for x in range(len(wordToFind)):
        # North-West: row decreases, column decreases
        guess1.append(crossword[row - x][coulmn - x])
    if guess1 == WTFlist:
        print(f'the first letter is in row {row}, coulmn {coulmn}')
    
if __name__ == "__main__":
    Crossword()





