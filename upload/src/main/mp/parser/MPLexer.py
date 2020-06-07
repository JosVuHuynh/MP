# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2A")
        buf.write("\u0295\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\4")
        buf.write("^\t^\4_\t_\4`\t`\3\2\3\2\3\2\3\2\7\2\u00c6\n\2\f\2\16")
        buf.write("\2\u00c9\13\2\3\2\3\2\3\3\3\3\3\3\3\3\7\3\u00d1\n\3\f")
        buf.write("\3\16\3\u00d4\13\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\7\4\u00dd")
        buf.write("\n\4\f\4\16\4\u00e0\13\4\3\4\3\4\3\4\3\4\3\5\3\5\5\5\u00e8")
        buf.write("\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37")
        buf.write("\3 \3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3$\3")
        buf.write("$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3")
        buf.write("-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3")
        buf.write("\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\3")
        buf.write("9\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\3>\3?\3?\3@\3@\3A\3A\3")
        buf.write("A\3B\3B\3B\3C\3C\3C\3D\3D\3E\3E\3F\3F\3G\3G\3H\3H\3I\3")
        buf.write("I\3J\3J\3K\3K\3L\3L\3M\3M\3N\3N\3O\3O\3O\3P\3P\3Q\6Q\u01ed")
        buf.write("\nQ\rQ\16Q\u01ee\3R\3R\3S\6S\u01f4\nS\rS\16S\u01f5\3S")
        buf.write("\3S\5S\u01fa\nS\3S\6S\u01fd\nS\rS\16S\u01fe\3T\7T\u0202")
        buf.write("\nT\fT\16T\u0205\13T\3T\3T\6T\u0209\nT\rT\16T\u020a\3")
        buf.write("T\3T\5T\u020f\nT\3T\6T\u0212\nT\rT\16T\u0213\3U\7U\u0217")
        buf.write("\nU\fU\16U\u021a\13U\3U\3U\6U\u021e\nU\rU\16U\u021f\3")
        buf.write("V\6V\u0223\nV\rV\16V\u0224\3V\3V\7V\u0229\nV\fV\16V\u022c")
        buf.write("\13V\3W\3W\3W\3W\5W\u0232\nW\3X\3X\5X\u0236\nX\3X\3X\3")
        buf.write("X\7X\u023b\nX\fX\16X\u023e\13X\3Y\6Y\u0241\nY\rY\16Y\u0242")
        buf.write("\3Y\3Y\3Z\3Z\3Z\7Z\u024a\nZ\fZ\16Z\u024d\13Z\3Z\3Z\3[")
        buf.write("\7[\u0252\n[\f[\16[\u0255\13[\3[\3[\3[\7[\u025a\n[\f[")
        buf.write("\16[\u025d\13[\3[\3[\3\\\3\\\3\\\7\\\u0264\n\\\f\\\16")
        buf.write("\\\u0267\13\\\3\\\3\\\3\\\3]\3]\3]\3]\3]\3]\3]\3]\3]\3")
        buf.write("]\3]\3]\3]\3]\3]\3]\3]\5]\u027d\n]\3^\3^\3^\3_\3_\7_\u0284")
        buf.write("\n_\f_\16_\u0287\13_\3_\3_\7_\u028b\n_\f_\16_\u028e\13")
        buf.write("_\3_\3_\3_\3`\3`\3`\b\u00d2\u00de\u0253\u025b\u0285\u028c")
        buf.write("\2a\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G\2I\2")
        buf.write("K\2M\2O\2Q\2S\2U\2W\2Y\2[\2]\2_\2a\2c\2e\2g\2i\2k\2m\2")
        buf.write("o\2q\2s\2u\2w\2y\2{%}&\177\'\u0081(\u0083)\u0085*\u0087")
        buf.write("+\u0089,\u008b-\u008d.\u008f/\u0091\60\u0093\61\u0095")
        buf.write("\62\u0097\63\u0099\64\u009b\65\u009d\66\u009f\67\u00a1")
        buf.write("8\u00a3\2\u00a5\2\u00a7\2\u00a9\2\u00ab\2\u00ad9\u00af")
        buf.write(":\u00b1;\u00b3<\u00b5=\u00b7>\u00b9?\u00bb\2\u00bd@\u00bf")
        buf.write("A\3\2#\4\2\f\f\17\17\4\2CCcc\4\2DDdd\4\2EEee\4\2FFff\4")
        buf.write("\2GGgg\4\2HHhh\4\2IIii\4\2JJjj\4\2KKkk\4\2LLll\4\2MMm")
        buf.write("m\4\2NNnn\4\2OOoo\4\2PPpp\4\2QQqq\4\2RRrr\4\2SSss\4\2")
        buf.write("TTtt\4\2UUuu\4\2VVvv\4\2WWww\4\2XXxx\4\2YYyy\4\2ZZzz\4")
        buf.write("\2[[{{\4\2\\\\||\3\2\62;\4\2C\\c|\5\2GGgg~~\5\2\13\f\16")
        buf.write("\17\"\"\6\2\f\f\17\17$$^^\n\2$$))^^ddhhppttvv\2\u029b")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2")
        buf.write("\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085")
        buf.write("\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2")
        buf.write("\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093")
        buf.write("\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2")
        buf.write("\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\2\u009f\3\2\2\2\2\u00a1")
        buf.write("\3\2\2\2\2\u00ad\3\2\2\2\2\u00af\3\2\2\2\2\u00b1\3\2\2")
        buf.write("\2\2\u00b3\3\2\2\2\2\u00b5\3\2\2\2\2\u00b7\3\2\2\2\2\u00b9")
        buf.write("\3\2\2\2\2\u00bd\3\2\2\2\2\u00bf\3\2\2\2\3\u00c1\3\2\2")
        buf.write("\2\5\u00cc\3\2\2\2\7\u00da\3\2\2\2\t\u00e7\3\2\2\2\13")
        buf.write("\u00e9\3\2\2\2\r\u00ef\3\2\2\2\17\u00f8\3\2\2\2\21\u00fc")
        buf.write("\3\2\2\2\23\u00ff\3\2\2\2\25\u0106\3\2\2\2\27\u0109\3")
        buf.write("\2\2\2\31\u010c\3\2\2\2\33\u0111\3\2\2\2\35\u0116\3\2")
        buf.write("\2\2\37\u011d\3\2\2\2!\u0123\3\2\2\2#\u0128\3\2\2\2%\u012e")
        buf.write("\3\2\2\2\'\u0132\3\2\2\2)\u013b\3\2\2\2+\u0145\3\2\2\2")
        buf.write("-\u0149\3\2\2\2/\u014e\3\2\2\2\61\u0154\3\2\2\2\63\u015a")
        buf.write("\3\2\2\2\65\u015d\3\2\2\2\67\u0162\3\2\2\29\u016a\3\2")
        buf.write("\2\2;\u0172\3\2\2\2=\u0179\3\2\2\2?\u017d\3\2\2\2A\u0181")
        buf.write("\3\2\2\2C\u0184\3\2\2\2E\u0188\3\2\2\2G\u018c\3\2\2\2")
        buf.write("I\u018e\3\2\2\2K\u0190\3\2\2\2M\u0192\3\2\2\2O\u0194\3")
        buf.write("\2\2\2Q\u0196\3\2\2\2S\u0198\3\2\2\2U\u019a\3\2\2\2W\u019c")
        buf.write("\3\2\2\2Y\u019e\3\2\2\2[\u01a0\3\2\2\2]\u01a2\3\2\2\2")
        buf.write("_\u01a4\3\2\2\2a\u01a6\3\2\2\2c\u01a8\3\2\2\2e\u01aa\3")
        buf.write("\2\2\2g\u01ac\3\2\2\2i\u01ae\3\2\2\2k\u01b0\3\2\2\2m\u01b2")
        buf.write("\3\2\2\2o\u01b4\3\2\2\2q\u01b6\3\2\2\2s\u01b8\3\2\2\2")
        buf.write("u\u01ba\3\2\2\2w\u01bc\3\2\2\2y\u01be\3\2\2\2{\u01c0\3")
        buf.write("\2\2\2}\u01c3\3\2\2\2\177\u01c5\3\2\2\2\u0081\u01c7\3")
        buf.write("\2\2\2\u0083\u01ca\3\2\2\2\u0085\u01cd\3\2\2\2\u0087\u01d0")
        buf.write("\3\2\2\2\u0089\u01d2\3\2\2\2\u008b\u01d4\3\2\2\2\u008d")
        buf.write("\u01d6\3\2\2\2\u008f\u01d8\3\2\2\2\u0091\u01da\3\2\2\2")
        buf.write("\u0093\u01dc\3\2\2\2\u0095\u01de\3\2\2\2\u0097\u01e0\3")
        buf.write("\2\2\2\u0099\u01e2\3\2\2\2\u009b\u01e4\3\2\2\2\u009d\u01e6")
        buf.write("\3\2\2\2\u009f\u01e9\3\2\2\2\u00a1\u01ec\3\2\2\2\u00a3")
        buf.write("\u01f0\3\2\2\2\u00a5\u01f3\3\2\2\2\u00a7\u0203\3\2\2\2")
        buf.write("\u00a9\u0218\3\2\2\2\u00ab\u0222\3\2\2\2\u00ad\u0231\3")
        buf.write("\2\2\2\u00af\u0235\3\2\2\2\u00b1\u0240\3\2\2\2\u00b3\u0246")
        buf.write("\3\2\2\2\u00b5\u0253\3\2\2\2\u00b7\u0260\3\2\2\2\u00b9")
        buf.write("\u026b\3\2\2\2\u00bb\u027e\3\2\2\2\u00bd\u0281\3\2\2\2")
        buf.write("\u00bf\u0292\3\2\2\2\u00c1\u00c2\7\61\2\2\u00c2\u00c3")
        buf.write("\7\61\2\2\u00c3\u00c7\3\2\2\2\u00c4\u00c6\n\2\2\2\u00c5")
        buf.write("\u00c4\3\2\2\2\u00c6\u00c9\3\2\2\2\u00c7\u00c5\3\2\2\2")
        buf.write("\u00c7\u00c8\3\2\2\2\u00c8\u00ca\3\2\2\2\u00c9\u00c7\3")
        buf.write("\2\2\2\u00ca\u00cb\b\2\2\2\u00cb\4\3\2\2\2\u00cc\u00cd")
        buf.write("\7*\2\2\u00cd\u00ce\7,\2\2\u00ce\u00d2\3\2\2\2\u00cf\u00d1")
        buf.write("\13\2\2\2\u00d0\u00cf\3\2\2\2\u00d1\u00d4\3\2\2\2\u00d2")
        buf.write("\u00d3\3\2\2\2\u00d2\u00d0\3\2\2\2\u00d3\u00d5\3\2\2\2")
        buf.write("\u00d4\u00d2\3\2\2\2\u00d5\u00d6\7,\2\2\u00d6\u00d7\7")
        buf.write("+\2\2\u00d7\u00d8\3\2\2\2\u00d8\u00d9\b\3\2\2\u00d9\6")
        buf.write("\3\2\2\2\u00da\u00de\7}\2\2\u00db\u00dd\13\2\2\2\u00dc")
        buf.write("\u00db\3\2\2\2\u00dd\u00e0\3\2\2\2\u00de\u00df\3\2\2\2")
        buf.write("\u00de\u00dc\3\2\2\2\u00df\u00e1\3\2\2\2\u00e0\u00de\3")
        buf.write("\2\2\2\u00e1\u00e2\7\177\2\2\u00e2\u00e3\3\2\2\2\u00e3")
        buf.write("\u00e4\b\4\2\2\u00e4\b\3\2\2\2\u00e5\u00e8\5-\27\2\u00e6")
        buf.write("\u00e8\5/\30\2\u00e7\u00e5\3\2\2\2\u00e7\u00e6\3\2\2\2")
        buf.write("\u00e8\n\3\2\2\2\u00e9\u00ea\5I%\2\u00ea\u00eb\5i\65\2")
        buf.write("\u00eb\u00ec\5O(\2\u00ec\u00ed\5G$\2\u00ed\u00ee\5[.\2")
        buf.write("\u00ee\f\3\2\2\2\u00ef\u00f0\5K&\2\u00f0\u00f1\5c\62\2")
        buf.write("\u00f1\u00f2\5a\61\2\u00f2\u00f3\5m\67\2\u00f3\u00f4\5")
        buf.write("W,\2\u00f4\u00f5\5a\61\2\u00f5\u00f6\5o8\2\u00f6\u00f7")
        buf.write("\5O(\2\u00f7\16\3\2\2\2\u00f8\u00f9\5Q)\2\u00f9\u00fa")
        buf.write("\5c\62\2\u00fa\u00fb\5i\65\2\u00fb\20\3\2\2\2\u00fc\u00fd")
        buf.write("\5m\67\2\u00fd\u00fe\5c\62\2\u00fe\22\3\2\2\2\u00ff\u0100")
        buf.write("\5M\'\2\u0100\u0101\5c\62\2\u0101\u0102\5s:\2\u0102\u0103")
        buf.write("\5a\61\2\u0103\u0104\5m\67\2\u0104\u0105\5c\62\2\u0105")
        buf.write("\24\3\2\2\2\u0106\u0107\5M\'\2\u0107\u0108\5c\62\2\u0108")
        buf.write("\26\3\2\2\2\u0109\u010a\5W,\2\u010a\u010b\5Q)\2\u010b")
        buf.write("\30\3\2\2\2\u010c\u010d\5m\67\2\u010d\u010e\5U+\2\u010e")
        buf.write("\u010f\5O(\2\u010f\u0110\5a\61\2\u0110\32\3\2\2\2\u0111")
        buf.write("\u0112\5O(\2\u0112\u0113\5]/\2\u0113\u0114\5k\66\2\u0114")
        buf.write("\u0115\5O(\2\u0115\34\3\2\2\2\u0116\u0117\5i\65\2\u0117")
        buf.write("\u0118\5O(\2\u0118\u0119\5m\67\2\u0119\u011a\5o8\2\u011a")
        buf.write("\u011b\5i\65\2\u011b\u011c\5a\61\2\u011c\36\3\2\2\2\u011d")
        buf.write("\u011e\5s:\2\u011e\u011f\5U+\2\u011f\u0120\5W,\2\u0120")
        buf.write("\u0121\5]/\2\u0121\u0122\5O(\2\u0122 \3\2\2\2\u0123\u0124")
        buf.write("\5s:\2\u0124\u0125\5W,\2\u0125\u0126\5m\67\2\u0126\u0127")
        buf.write("\5U+\2\u0127\"\3\2\2\2\u0128\u0129\5I%\2\u0129\u012a\5")
        buf.write("O(\2\u012a\u012b\5S*\2\u012b\u012c\5W,\2\u012c\u012d\5")
        buf.write("a\61\2\u012d$\3\2\2\2\u012e\u012f\5O(\2\u012f\u0130\5")
        buf.write("a\61\2\u0130\u0131\5M\'\2\u0131&\3\2\2\2\u0132\u0133\5")
        buf.write("Q)\2\u0133\u0134\5o8\2\u0134\u0135\5a\61\2\u0135\u0136")
        buf.write("\5K&\2\u0136\u0137\5m\67\2\u0137\u0138\5W,\2\u0138\u0139")
        buf.write("\5c\62\2\u0139\u013a\5a\61\2\u013a(\3\2\2\2\u013b\u013c")
        buf.write("\5e\63\2\u013c\u013d\5i\65\2\u013d\u013e\5c\62\2\u013e")
        buf.write("\u013f\5K&\2\u013f\u0140\5O(\2\u0140\u0141\5M\'\2\u0141")
        buf.write("\u0142\5o8\2\u0142\u0143\5i\65\2\u0143\u0144\5O(\2\u0144")
        buf.write("*\3\2\2\2\u0145\u0146\5q9\2\u0146\u0147\5G$\2\u0147\u0148")
        buf.write("\5i\65\2\u0148,\3\2\2\2\u0149\u014a\5m\67\2\u014a\u014b")
        buf.write("\5i\65\2\u014b\u014c\5o8\2\u014c\u014d\5O(\2\u014d.\3")
        buf.write("\2\2\2\u014e\u014f\5Q)\2\u014f\u0150\5G$\2\u0150\u0151")
        buf.write("\5]/\2\u0151\u0152\5k\66\2\u0152\u0153\5O(\2\u0153\60")
        buf.write("\3\2\2\2\u0154\u0155\5G$\2\u0155\u0156\5i\65\2\u0156\u0157")
        buf.write("\5i\65\2\u0157\u0158\5G$\2\u0158\u0159\5w<\2\u0159\62")
        buf.write("\3\2\2\2\u015a\u015b\5c\62\2\u015b\u015c\5Q)\2\u015c\64")
        buf.write("\3\2\2\2\u015d\u015e\5i\65\2\u015e\u015f\5O(\2\u015f\u0160")
        buf.write("\5G$\2\u0160\u0161\5]/\2\u0161\66\3\2\2\2\u0162\u0163")
        buf.write("\5I%\2\u0163\u0164\5c\62\2\u0164\u0165\5c\62\2\u0165\u0166")
        buf.write("\5]/\2\u0166\u0167\5O(\2\u0167\u0168\5G$\2\u0168\u0169")
        buf.write("\5a\61\2\u01698\3\2\2\2\u016a\u016b\5W,\2\u016b\u016c")
        buf.write("\5a\61\2\u016c\u016d\5m\67\2\u016d\u016e\5O(\2\u016e\u016f")
        buf.write("\5S*\2\u016f\u0170\5O(\2\u0170\u0171\5i\65\2\u0171:\3")
        buf.write("\2\2\2\u0172\u0173\5k\66\2\u0173\u0174\5m\67\2\u0174\u0175")
        buf.write("\5i\65\2\u0175\u0176\5W,\2\u0176\u0177\5a\61\2\u0177\u0178")
        buf.write("\5S*\2\u0178<\3\2\2\2\u0179\u017a\5a\61\2\u017a\u017b")
        buf.write("\5c\62\2\u017b\u017c\5m\67\2\u017c>\3\2\2\2\u017d\u017e")
        buf.write("\5G$\2\u017e\u017f\5a\61\2\u017f\u0180\5M\'\2\u0180@\3")
        buf.write("\2\2\2\u0181\u0182\5c\62\2\u0182\u0183\5i\65\2\u0183B")
        buf.write("\3\2\2\2\u0184\u0185\5M\'\2\u0185\u0186\5W,\2\u0186\u0187")
        buf.write("\5q9\2\u0187D\3\2\2\2\u0188\u0189\5_\60\2\u0189\u018a")
        buf.write("\5c\62\2\u018a\u018b\5M\'\2\u018bF\3\2\2\2\u018c\u018d")
        buf.write("\t\3\2\2\u018dH\3\2\2\2\u018e\u018f\t\4\2\2\u018fJ\3\2")
        buf.write("\2\2\u0190\u0191\t\5\2\2\u0191L\3\2\2\2\u0192\u0193\t")
        buf.write("\6\2\2\u0193N\3\2\2\2\u0194\u0195\t\7\2\2\u0195P\3\2\2")
        buf.write("\2\u0196\u0197\t\b\2\2\u0197R\3\2\2\2\u0198\u0199\t\t")
        buf.write("\2\2\u0199T\3\2\2\2\u019a\u019b\t\n\2\2\u019bV\3\2\2\2")
        buf.write("\u019c\u019d\t\13\2\2\u019dX\3\2\2\2\u019e\u019f\t\f\2")
        buf.write("\2\u019fZ\3\2\2\2\u01a0\u01a1\t\r\2\2\u01a1\\\3\2\2\2")
        buf.write("\u01a2\u01a3\t\16\2\2\u01a3^\3\2\2\2\u01a4\u01a5\t\17")
        buf.write("\2\2\u01a5`\3\2\2\2\u01a6\u01a7\t\20\2\2\u01a7b\3\2\2")
        buf.write("\2\u01a8\u01a9\t\21\2\2\u01a9d\3\2\2\2\u01aa\u01ab\t\22")
        buf.write("\2\2\u01abf\3\2\2\2\u01ac\u01ad\t\23\2\2\u01adh\3\2\2")
        buf.write("\2\u01ae\u01af\t\24\2\2\u01afj\3\2\2\2\u01b0\u01b1\t\25")
        buf.write("\2\2\u01b1l\3\2\2\2\u01b2\u01b3\t\26\2\2\u01b3n\3\2\2")
        buf.write("\2\u01b4\u01b5\t\27\2\2\u01b5p\3\2\2\2\u01b6\u01b7\t\30")
        buf.write("\2\2\u01b7r\3\2\2\2\u01b8\u01b9\t\31\2\2\u01b9t\3\2\2")
        buf.write("\2\u01ba\u01bb\t\32\2\2\u01bbv\3\2\2\2\u01bc\u01bd\t\33")
        buf.write("\2\2\u01bdx\3\2\2\2\u01be\u01bf\t\34\2\2\u01bfz\3\2\2")
        buf.write("\2\u01c0\u01c1\7<\2\2\u01c1\u01c2\7?\2\2\u01c2|\3\2\2")
        buf.write("\2\u01c3\u01c4\7-\2\2\u01c4~\3\2\2\2\u01c5\u01c6\7,\2")
        buf.write("\2\u01c6\u0080\3\2\2\2\u01c7\u01c8\7>\2\2\u01c8\u01c9")
        buf.write("\7@\2\2\u01c9\u0082\3\2\2\2\u01ca\u01cb\7>\2\2\u01cb\u01cc")
        buf.write("\7?\2\2\u01cc\u0084\3\2\2\2\u01cd\u01ce\7@\2\2\u01ce\u01cf")
        buf.write("\7?\2\2\u01cf\u0086\3\2\2\2\u01d0\u01d1\7/\2\2\u01d1\u0088")
        buf.write("\3\2\2\2\u01d2\u01d3\7\61\2\2\u01d3\u008a\3\2\2\2\u01d4")
        buf.write("\u01d5\7?\2\2\u01d5\u008c\3\2\2\2\u01d6\u01d7\7>\2\2\u01d7")
        buf.write("\u008e\3\2\2\2\u01d8\u01d9\7@\2\2\u01d9\u0090\3\2\2\2")
        buf.write("\u01da\u01db\7]\2\2\u01db\u0092\3\2\2\2\u01dc\u01dd\7")
        buf.write("_\2\2\u01dd\u0094\3\2\2\2\u01de\u01df\7<\2\2\u01df\u0096")
        buf.write("\3\2\2\2\u01e0\u01e1\7*\2\2\u01e1\u0098\3\2\2\2\u01e2")
        buf.write("\u01e3\7+\2\2\u01e3\u009a\3\2\2\2\u01e4\u01e5\7=\2\2\u01e5")
        buf.write("\u009c\3\2\2\2\u01e6\u01e7\7\60\2\2\u01e7\u01e8\7\60\2")
        buf.write("\2\u01e8\u009e\3\2\2\2\u01e9\u01ea\7.\2\2\u01ea\u00a0")
        buf.write("\3\2\2\2\u01eb\u01ed\t\35\2\2\u01ec\u01eb\3\2\2\2\u01ed")
        buf.write("\u01ee\3\2\2\2\u01ee\u01ec\3\2\2\2\u01ee\u01ef\3\2\2\2")
        buf.write("\u01ef\u00a2\3\2\2\2\u01f0\u01f1\t\36\2\2\u01f1\u00a4")
        buf.write("\3\2\2\2\u01f2\u01f4\t\35\2\2\u01f3\u01f2\3\2\2\2\u01f4")
        buf.write("\u01f5\3\2\2\2\u01f5\u01f3\3\2\2\2\u01f5\u01f6\3\2\2\2")
        buf.write("\u01f6\u01f7\3\2\2\2\u01f7\u01f9\t\37\2\2\u01f8\u01fa")
        buf.write("\7/\2\2\u01f9\u01f8\3\2\2\2\u01f9\u01fa\3\2\2\2\u01fa")
        buf.write("\u01fc\3\2\2\2\u01fb\u01fd\t\35\2\2\u01fc\u01fb\3\2\2")
        buf.write("\2\u01fd\u01fe\3\2\2\2\u01fe\u01fc\3\2\2\2\u01fe\u01ff")
        buf.write("\3\2\2\2\u01ff\u00a6\3\2\2\2\u0200\u0202\t\35\2\2\u0201")
        buf.write("\u0200\3\2\2\2\u0202\u0205\3\2\2\2\u0203\u0201\3\2\2\2")
        buf.write("\u0203\u0204\3\2\2\2\u0204\u0206\3\2\2\2\u0205\u0203\3")
        buf.write("\2\2\2\u0206\u0208\7\60\2\2\u0207\u0209\t\35\2\2\u0208")
        buf.write("\u0207\3\2\2\2\u0209\u020a\3\2\2\2\u020a\u0208\3\2\2\2")
        buf.write("\u020a\u020b\3\2\2\2\u020b\u020c\3\2\2\2\u020c\u020e\t")
        buf.write("\37\2\2\u020d\u020f\7/\2\2\u020e\u020d\3\2\2\2\u020e\u020f")
        buf.write("\3\2\2\2\u020f\u0211\3\2\2\2\u0210\u0212\t\35\2\2\u0211")
        buf.write("\u0210\3\2\2\2\u0212\u0213\3\2\2\2\u0213\u0211\3\2\2\2")
        buf.write("\u0213\u0214\3\2\2\2\u0214\u00a8\3\2\2\2\u0215\u0217\t")
        buf.write("\35\2\2\u0216\u0215\3\2\2\2\u0217\u021a\3\2\2\2\u0218")
        buf.write("\u0216\3\2\2\2\u0218\u0219\3\2\2\2\u0219\u021b\3\2\2\2")
        buf.write("\u021a\u0218\3\2\2\2\u021b\u021d\7\60\2\2\u021c\u021e")
        buf.write("\t\35\2\2\u021d\u021c\3\2\2\2\u021e\u021f\3\2\2\2\u021f")
        buf.write("\u021d\3\2\2\2\u021f\u0220\3\2\2\2\u0220\u00aa\3\2\2\2")
        buf.write("\u0221\u0223\t\35\2\2\u0222\u0221\3\2\2\2\u0223\u0224")
        buf.write("\3\2\2\2\u0224\u0222\3\2\2\2\u0224\u0225\3\2\2\2\u0225")
        buf.write("\u0226\3\2\2\2\u0226\u022a\7\60\2\2\u0227\u0229\t\35\2")
        buf.write("\2\u0228\u0227\3\2\2\2\u0229\u022c\3\2\2\2\u022a\u0228")
        buf.write("\3\2\2\2\u022a\u022b\3\2\2\2\u022b\u00ac\3\2\2\2\u022c")
        buf.write("\u022a\3\2\2\2\u022d\u0232\5\u00a5S\2\u022e\u0232\5\u00a7")
        buf.write("T\2\u022f\u0232\5\u00a9U\2\u0230\u0232\5\u00abV\2\u0231")
        buf.write("\u022d\3\2\2\2\u0231\u022e\3\2\2\2\u0231\u022f\3\2\2\2")
        buf.write("\u0231\u0230\3\2\2\2\u0232\u00ae\3\2\2\2\u0233\u0236\7")
        buf.write("a\2\2\u0234\u0236\5\u00a3R\2\u0235\u0233\3\2\2\2\u0235")
        buf.write("\u0234\3\2\2\2\u0236\u023c\3\2\2\2\u0237\u023b\7a\2\2")
        buf.write("\u0238\u023b\5\u00a3R\2\u0239\u023b\t\35\2\2\u023a\u0237")
        buf.write("\3\2\2\2\u023a\u0238\3\2\2\2\u023a\u0239\3\2\2\2\u023b")
        buf.write("\u023e\3\2\2\2\u023c\u023a\3\2\2\2\u023c\u023d\3\2\2\2")
        buf.write("\u023d\u00b0\3\2\2\2\u023e\u023c\3\2\2\2\u023f\u0241\t")
        buf.write(" \2\2\u0240\u023f\3\2\2\2\u0241\u0242\3\2\2\2\u0242\u0240")
        buf.write("\3\2\2\2\u0242\u0243\3\2\2\2\u0243\u0244\3\2\2\2\u0244")
        buf.write("\u0245\bY\2\2\u0245\u00b2\3\2\2\2\u0246\u024b\7$\2\2\u0247")
        buf.write("\u024a\5\u00b9]\2\u0248\u024a\n!\2\2\u0249\u0247\3\2\2")
        buf.write("\2\u0249\u0248\3\2\2\2\u024a\u024d\3\2\2\2\u024b\u0249")
        buf.write("\3\2\2\2\u024b\u024c\3\2\2\2\u024c\u024e\3\2\2\2\u024d")
        buf.write("\u024b\3\2\2\2\u024e\u024f\bZ\3\2\u024f\u00b4\3\2\2\2")
        buf.write("\u0250\u0252\13\2\2\2\u0251\u0250\3\2\2\2\u0252\u0255")
        buf.write("\3\2\2\2\u0253\u0254\3\2\2\2\u0253\u0251\3\2\2\2\u0254")
        buf.write("\u0256\3\2\2\2\u0255\u0253\3\2\2\2\u0256\u0257\7^\2\2")
        buf.write("\u0257\u025b\t\"\2\2\u0258\u025a\13\2\2\2\u0259\u0258")
        buf.write("\3\2\2\2\u025a\u025d\3\2\2\2\u025b\u025c\3\2\2\2\u025b")
        buf.write("\u0259\3\2\2\2\u025c\u025e\3\2\2\2\u025d\u025b\3\2\2\2")
        buf.write("\u025e\u025f\b[\4\2\u025f\u00b6\3\2\2\2\u0260\u0265\7")
        buf.write("$\2\2\u0261\u0264\5\u00b9]\2\u0262\u0264\n!\2\2\u0263")
        buf.write("\u0261\3\2\2\2\u0263\u0262\3\2\2\2\u0264\u0267\3\2\2\2")
        buf.write("\u0265\u0263\3\2\2\2\u0265\u0266\3\2\2\2\u0266\u0268\3")
        buf.write("\2\2\2\u0267\u0265\3\2\2\2\u0268\u0269\7$\2\2\u0269\u026a")
        buf.write("\b\\\5\2\u026a\u00b8\3\2\2\2\u026b\u027c\7^\2\2\u026c")
        buf.write("\u026d\7d\2\2\u026d\u027d\b]\6\2\u026e\u026f\7h\2\2\u026f")
        buf.write("\u027d\b]\7\2\u0270\u0271\7t\2\2\u0271\u027d\b]\b\2\u0272")
        buf.write("\u0273\7p\2\2\u0273\u027d\b]\t\2\u0274\u0275\7v\2\2\u0275")
        buf.write("\u027d\b]\n\2\u0276\u0277\7)\2\2\u0277\u027d\b]\13\2\u0278")
        buf.write("\u0279\7$\2\2\u0279\u027d\b]\f\2\u027a\u027b\7^\2\2\u027b")
        buf.write("\u027d\b]\r\2\u027c\u026c\3\2\2\2\u027c\u026e\3\2\2\2")
        buf.write("\u027c\u0270\3\2\2\2\u027c\u0272\3\2\2\2\u027c\u0274\3")
        buf.write("\2\2\2\u027c\u0276\3\2\2\2\u027c\u0278\3\2\2\2\u027c\u027a")
        buf.write("\3\2\2\2\u027d\u00ba\3\2\2\2\u027e\u027f\7^\2\2\u027f")
        buf.write("\u0280\n\"\2\2\u0280\u00bc\3\2\2\2\u0281\u0285\7$\2\2")
        buf.write("\u0282\u0284\13\2\2\2\u0283\u0282\3\2\2\2\u0284\u0287")
        buf.write("\3\2\2\2\u0285\u0286\3\2\2\2\u0285\u0283\3\2\2\2\u0286")
        buf.write("\u0288\3\2\2\2\u0287\u0285\3\2\2\2\u0288\u028c\5\u00bb")
        buf.write("^\2\u0289\u028b\13\2\2\2\u028a\u0289\3\2\2\2\u028b\u028e")
        buf.write("\3\2\2\2\u028c\u028d\3\2\2\2\u028c\u028a\3\2\2\2\u028d")
        buf.write("\u028f\3\2\2\2\u028e\u028c\3\2\2\2\u028f\u0290\7$\2\2")
        buf.write("\u0290\u0291\b_\16\2\u0291\u00be\3\2\2\2\u0292\u0293\13")
        buf.write("\2\2\2\u0293\u0294\b`\17\2\u0294\u00c0\3\2\2\2!\2\u00c7")
        buf.write("\u00d2\u00de\u00e7\u01ee\u01f5\u01f9\u01fe\u0203\u020a")
        buf.write("\u020e\u0213\u0218\u021f\u0224\u022a\u0231\u0235\u023a")
        buf.write("\u023c\u0242\u0249\u024b\u0253\u025b\u0263\u0265\u027c")
        buf.write("\u0285\u028c\20\b\2\2\3Z\2\3[\3\3\\\4\3]\5\3]\6\3]\7\3")
        buf.write("]\b\3]\t\3]\n\3]\13\3]\f\3_\r\3`\16")
        return buf.getvalue()


class MPLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    LINE_COMMENT = 1
    TRA_BLOCK_COMMENT = 2
    BLOCK_COMMENT = 3
    BOOLEANLIT = 4
    BREAK = 5
    CONTINUE = 6
    FOR = 7
    TO = 8
    DOWNTO = 9
    DO = 10
    IF = 11
    THEN = 12
    ELSE = 13
    RETURN = 14
    WHILE = 15
    WITH = 16
    BEGIN = 17
    END = 18
    FUNCTION = 19
    PROCEDURE = 20
    VAR = 21
    TRUE = 22
    FALSE = 23
    ARRAY = 24
    OF = 25
    REALTYPE = 26
    BOOLEANTYPE = 27
    INTTYPE = 28
    STRINGTYPE = 29
    NOT = 30
    AND = 31
    OR = 32
    DIV = 33
    MOD = 34
    ASSIGN = 35
    ADD = 36
    MUL = 37
    NOTEQUAL = 38
    LESSOREQUAL = 39
    GREATEROREQUAL = 40
    SUB = 41
    DIVISION = 42
    EQUAL = 43
    LESS = 44
    GREATER = 45
    LSB = 46
    RSB = 47
    COLON = 48
    LB = 49
    RB = 50
    SM = 51
    DD = 52
    CM = 53
    INTLIT = 54
    FLOATLIT = 55
    ID = 56
    WS = 57
    UNCLOSE_STRING = 58
    ERR = 59
    STRINGLIT = 60
    ESCAPE = 61
    ILLEGAL_ESCAPE = 62
    ERROR_CHAR = 63

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':='", "'+'", "'*'", "'<>'", "'<='", "'>='", "'-'", "'/'", 
            "'='", "'<'", "'>'", "'['", "']'", "':'", "'('", "')'", "';'", 
            "'..'", "','" ]

    symbolicNames = [ "<INVALID>",
            "LINE_COMMENT", "TRA_BLOCK_COMMENT", "BLOCK_COMMENT", "BOOLEANLIT", 
            "BREAK", "CONTINUE", "FOR", "TO", "DOWNTO", "DO", "IF", "THEN", 
            "ELSE", "RETURN", "WHILE", "WITH", "BEGIN", "END", "FUNCTION", 
            "PROCEDURE", "VAR", "TRUE", "FALSE", "ARRAY", "OF", "REALTYPE", 
            "BOOLEANTYPE", "INTTYPE", "STRINGTYPE", "NOT", "AND", "OR", 
            "DIV", "MOD", "ASSIGN", "ADD", "MUL", "NOTEQUAL", "LESSOREQUAL", 
            "GREATEROREQUAL", "SUB", "DIVISION", "EQUAL", "LESS", "GREATER", 
            "LSB", "RSB", "COLON", "LB", "RB", "SM", "DD", "CM", "INTLIT", 
            "FLOATLIT", "ID", "WS", "UNCLOSE_STRING", "ERR", "STRINGLIT", 
            "ESCAPE", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "LINE_COMMENT", "TRA_BLOCK_COMMENT", "BLOCK_COMMENT", 
                  "BOOLEANLIT", "BREAK", "CONTINUE", "FOR", "TO", "DOWNTO", 
                  "DO", "IF", "THEN", "ELSE", "RETURN", "WHILE", "WITH", 
                  "BEGIN", "END", "FUNCTION", "PROCEDURE", "VAR", "TRUE", 
                  "FALSE", "ARRAY", "OF", "REALTYPE", "BOOLEANTYPE", "INTTYPE", 
                  "STRINGTYPE", "NOT", "AND", "OR", "DIV", "MOD", "A", "B", 
                  "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
                  "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", 
                  "Y", "Z", "ASSIGN", "ADD", "MUL", "NOTEQUAL", "LESSOREQUAL", 
                  "GREATEROREQUAL", "SUB", "DIVISION", "EQUAL", "LESS", 
                  "GREATER", "LSB", "RSB", "COLON", "LB", "RB", "SM", "DD", 
                  "CM", "INTLIT", "LETTER", "CASE1", "CASE2", "CASE3", "CASE4", 
                  "FLOATLIT", "ID", "WS", "UNCLOSE_STRING", "ERR", "STRINGLIT", 
                  "ESCAPE", "ILL", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    grammarFileName = "MP.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[88] = self.UNCLOSE_STRING_action 
            actions[89] = self.ERR_action 
            actions[90] = self.STRINGLIT_action 
            actions[91] = self.ESCAPE_action 
            actions[93] = self.ILLEGAL_ESCAPE_action 
            actions[94] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
             
              raise UncloseString(self.text[1:])

     

    def ERR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

              raise ErrorToken('\\')

     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
             
             temp=Lexer.text.fget(self)
             temp1=(temp[1:len(temp)-1])
             Lexer.text.fset(self,temp1)

     

    def ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            Lexer.text.fset(self,"\b")
     

        if actionIndex == 4:
            Lexer.text.fset(self,"\f")
     

        if actionIndex == 5:
            Lexer.text.fset(self,"\r")
     

        if actionIndex == 6:
            Lexer.text.fset(self,"\n")
     

        if actionIndex == 7:
            Lexer.text.fset(self,"\t")
     

        if actionIndex == 8:
            Lexer.text.fset(self,"\'")
     

        if actionIndex == 9:
            Lexer.text.fset(self,"\"")
     

        if actionIndex == 10:
            Lexer.text.fset(self,"\\")
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 11:
                
             temp=Lexer.text.fget(self) 
             temp1=temp.find('\\')
             raise IllegalEscape(self.text[1:temp1+2])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 12:

             raise ErrorToken(self.text)

     


