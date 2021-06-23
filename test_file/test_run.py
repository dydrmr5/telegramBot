import peribahasa
import menu_reply

def test_command():
    assert peribahasa.getKategoriPeribahasa('test_command')
    assert peribahasa.getBidal()
    assert peribahasa.getPepatah()
    assert peribahasa.getPerumpamaan()
    assert peribahasa.getSemboyan()
    assert peribahasa.getTamsil()

def test_reply_command():
    assert menu_reply.botStart()
    assert menu_reply.botGreetings()
    assert menu_reply.botShowMenu()
    assert menu_reply.botShowPeribahasa()
