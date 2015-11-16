from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
     Number, Operator, Generic

class IdleClassicStyle(Style):
    default_style = ""
    styles = {
        Operator:               '#000',
        Number:                 '#000',
        Generic:                '#000',
        Keyword:                '#F70',
        Keyword.Pseudo:         '#900090',
        Keyword.Constant:       '#900090',
        Comment:                '#D00',
        Name:                   '#000',
        Name.Function:          '#00F',
        Name.Class:             '#00F',
        String:                 '#0A0',
        Error:                  'bg: #F30',
    }
