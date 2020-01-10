def correct_tail(body, tail):
    sub=body[len(body)-1]
    if sub==tail:
        print(True)
        return True
    else:
        print(False)
        return False

correct_tail('test','t')