# coding: utf-8

"""
    Strava API v3

    Strava API  # noqa: E501

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.zone_range import ZoneRange  # noqa: F401,E501


class TimedZoneRange(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'min': 'int',
        'max': 'int',
        'time': 'int'
    }

    attribute_map = {
        'min': 'min',
        'max': 'max',
        'time': 'time'
    }

    def __init__(self, min=None, max=None, time=None):  # noqa: E501
        """TimedZoneRange - a model defined in Swagger"""  # noqa: E501

        self._min = None
        self._max = None
        self._time = None
        self.discriminator = None

        if min is not None:
            self.min = min
        if max is not None:
            self.max = max
        if time is not None:
            self.time = time

    @property
    def min(self):
        """Gets the min of this TimedZoneRange.  # noqa: E501

        The minimum value in the range.  # noqa: E501

        :return: The min of this TimedZoneRange.  # noqa: E501
        :rtype: int
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this TimedZoneRange.

        The minimum value in the range.  # noqa: E501

        :param min: The min of this TimedZoneRange.  # noqa: E501
        :type: int
        """

        self._min = min

    @property
    def max(self):
        """Gets the max of this TimedZoneRange.  # noqa: E501

        The maximum value in the range.  # noqa: E501

        :return: The max of this TimedZoneRange.  # noqa: E501
        :rtype: int
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this TimedZoneRange.

        The maximum value in the range.  # noqa: E501

        :param max: The max of this TimedZoneRange.  # noqa: E501
        :type: int
        """

        self._max = max

    @property
    def time(self):
        """Gets the time of this TimedZoneRange.  # noqa: E501

        The number of seconds spent in this zone  # noqa: E501

        :return: The time of this TimedZoneRange.  # noqa: E501
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this TimedZoneRange.

        The number of seconds spent in this zone  # noqa: E501

        :param time: The time of this TimedZoneRange.  # noqa: E501
        :type: int
        """

        self._time = time

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TimedZoneRange):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
