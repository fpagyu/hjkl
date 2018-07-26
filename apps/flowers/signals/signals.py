# coding: utf-8
import flask.signals

my_signals = flask.signals.Namespace()

model_saved = my_signals.signal('model-saved')
