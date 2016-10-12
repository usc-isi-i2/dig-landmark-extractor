# -*- coding: utf-8 -*-
"""Module for defining an extractor that accepts a list of tokens
and outputs tokens that exist in a user provided trie"""
import copy

from itertools import ifilter
from itertools import tee
from itertools import chain
from itertools import izip
from digExtractor.extractor import Extractor
from landmark_extractor.extraction.Landmark import Rule
from landmark_extractor.extraction.Landmark import flattenResult

class DigLandmarkExtractor(Extractor):

    def __init__(self):
        self.renamed_input_fields = 'html'
        self.rule = None

    def get_rule(self):
        return self.rule

    def set_rule(self, rule):
        if not isinstance(rule, Rule):
            raise ValueError("rule must be a Rule")
        self.rule = rule
        return self

    def extract(self, doc):
            extracts = list()
            html = doc['html']
            result = self.rule.apply(html)
            result = flattenResult(result)
            return result

    def get_metadata(self):
        """Returns a copy of the metadata that characterizes this extractor"""
        return copy.copy(self.metadata)

    def set_metadata(self, metadata):
        """Overwrite the metadata that characterizes this extractor"""
        self.metadata = metadata
        return self

    def get_renamed_input_fields(self):
        """Return a scalar or ordered list of fields to rename to"""
        return self.renamed_input_fields
