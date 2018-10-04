# coding: utf-8

"""
    Strava API v3

    Strava API  # noqa: E501

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class SegmentsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def explore_segments(self, bounds, **kwargs):  # noqa: E501
        """Explore segments  # noqa: E501

        Returns the top 10 segments matching a specified query.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.explore_segments(bounds, async=True)
        >>> result = thread.get()

        :param async bool
        :param list[float] bounds: The latitude and longitude for two points describing a rectangular boundary for the search: [southwest corner latitutde, southwest corner longitude, northeast corner latitude, northeast corner longitude] (required)
        :param str activity_type: Desired activity type.
        :param int min_cat: The minimum climbing category.
        :param int max_cat: The maximum climbing category.
        :return: ExplorerResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.explore_segments_with_http_info(bounds, **kwargs)  # noqa: E501
        else:
            (data) = self.explore_segments_with_http_info(bounds, **kwargs)  # noqa: E501
            return data

    def explore_segments_with_http_info(self, bounds, **kwargs):  # noqa: E501
        """Explore segments  # noqa: E501

        Returns the top 10 segments matching a specified query.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.explore_segments_with_http_info(bounds, async=True)
        >>> result = thread.get()

        :param async bool
        :param list[float] bounds: The latitude and longitude for two points describing a rectangular boundary for the search: [southwest corner latitutde, southwest corner longitude, northeast corner latitude, northeast corner longitude] (required)
        :param str activity_type: Desired activity type.
        :param int min_cat: The minimum climbing category.
        :param int max_cat: The maximum climbing category.
        :return: ExplorerResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['bounds', 'activity_type', 'min_cat', 'max_cat']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method explore_segments" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'bounds' is set
        if ('bounds' not in params or
                params['bounds'] is None):
            raise ValueError("Missing the required parameter `bounds` when calling `explore_segments`")  # noqa: E501

        if ('bounds' in params and
                len(params['bounds']) > 4):
            raise ValueError("Invalid value for parameter `bounds` when calling `explore_segments`, number of items must be less than or equal to `4`")  # noqa: E501
        if ('bounds' in params and
                len(params['bounds']) < 4):
            raise ValueError("Invalid value for parameter `bounds` when calling `explore_segments`, number of items must be greater than or equal to `4`")  # noqa: E501
        if 'min_cat' in params and params['min_cat'] > 5:  # noqa: E501
            raise ValueError("Invalid value for parameter `min_cat` when calling `explore_segments`, must be a value less than or equal to `5`")  # noqa: E501
        if 'min_cat' in params and params['min_cat'] < 0:  # noqa: E501
            raise ValueError("Invalid value for parameter `min_cat` when calling `explore_segments`, must be a value greater than or equal to `0`")  # noqa: E501
        if 'max_cat' in params and params['max_cat'] > 5:  # noqa: E501
            raise ValueError("Invalid value for parameter `max_cat` when calling `explore_segments`, must be a value less than or equal to `5`")  # noqa: E501
        if 'max_cat' in params and params['max_cat'] < 0:  # noqa: E501
            raise ValueError("Invalid value for parameter `max_cat` when calling `explore_segments`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'bounds' in params:
            query_params.append(('bounds', params['bounds']))  # noqa: E501
            collection_formats['bounds'] = 'csv'  # noqa: E501
        if 'activity_type' in params:
            query_params.append(('activity_type', params['activity_type']))  # noqa: E501
        if 'min_cat' in params:
            query_params.append(('min_cat', params['min_cat']))  # noqa: E501
        if 'max_cat' in params:
            query_params.append(('max_cat', params['max_cat']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['strava_oauth']  # noqa: E501

        return self.api_client.call_api(
            '/segments/explore', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ExplorerResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_leaderboard_by_segment_id(self, id, **kwargs):  # noqa: E501
        """Get Segment Leaderboard  # noqa: E501

        Returns the specified segment leaderboard.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_leaderboard_by_segment_id(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the segment leaderboard. (required)
        :param str gender: Filter by gender.
        :param str age_group: Summit Feature. Filter by age group.
        :param str weight_class: Summit Feature. Filter by weight class.
        :param bool following: Filter by friends of the authenticated athlete.
        :param int club_id: Filter by club.
        :param str date_range: Filter by date range.
        :param int context_entries:
        :param int page: Page number.
        :param int per_page: Number of items per page. Defaults to 30.
        :return: SegmentLeaderboard
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_leaderboard_by_segment_id_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_leaderboard_by_segment_id_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_leaderboard_by_segment_id_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get Segment Leaderboard  # noqa: E501

        Returns the specified segment leaderboard.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_leaderboard_by_segment_id_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the segment leaderboard. (required)
        :param str gender: Filter by gender.
        :param str age_group: Summit Feature. Filter by age group.
        :param str weight_class: Summit Feature. Filter by weight class.
        :param bool following: Filter by friends of the authenticated athlete.
        :param int club_id: Filter by club.
        :param str date_range: Filter by date range.
        :param int context_entries:
        :param int page: Page number.
        :param int per_page: Number of items per page. Defaults to 30.
        :return: SegmentLeaderboard
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'gender', 'age_group', 'weight_class', 'following', 'club_id', 'date_range', 'context_entries', 'page', 'per_page']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_leaderboard_by_segment_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_leaderboard_by_segment_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'gender' in params:
            query_params.append(('gender', params['gender']))  # noqa: E501
        if 'age_group' in params:
            query_params.append(('age_group', params['age_group']))  # noqa: E501
        if 'weight_class' in params:
            query_params.append(('weight_class', params['weight_class']))  # noqa: E501
        if 'following' in params:
            query_params.append(('following', params['following']))  # noqa: E501
        if 'club_id' in params:
            query_params.append(('club_id', params['club_id']))  # noqa: E501
        if 'date_range' in params:
            query_params.append(('date_range', params['date_range']))  # noqa: E501
        if 'context_entries' in params:
            query_params.append(('context_entries', params['context_entries']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'per_page' in params:
            query_params.append(('per_page', params['per_page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['strava_oauth']  # noqa: E501

        return self.api_client.call_api(
            '/segments/{id}/leaderboard', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SegmentLeaderboard',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_logged_in_athlete_starred_segments(self, **kwargs):  # noqa: E501
        """List Starred Segments  # noqa: E501

        List of the authenticated athlete's starred segments.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_logged_in_athlete_starred_segments(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: Page number.
        :param int per_page: Number of items per page. Defaults to 30.
        :return: list[SummarySegment]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_logged_in_athlete_starred_segments_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_logged_in_athlete_starred_segments_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_logged_in_athlete_starred_segments_with_http_info(self, **kwargs):  # noqa: E501
        """List Starred Segments  # noqa: E501

        List of the authenticated athlete's starred segments.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_logged_in_athlete_starred_segments_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: Page number.
        :param int per_page: Number of items per page. Defaults to 30.
        :return: list[SummarySegment]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'per_page']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_logged_in_athlete_starred_segments" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'per_page' in params:
            query_params.append(('per_page', params['per_page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['strava_oauth']  # noqa: E501

        return self.api_client.call_api(
            '/segments/starred', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SummarySegment]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_segment_by_id(self, id, **kwargs):  # noqa: E501
        """Get Segment  # noqa: E501

        Returns the specified segment.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_segment_by_id(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the segment. (required)
        :return: DetailedSegment
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_segment_by_id_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_segment_by_id_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_segment_by_id_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get Segment  # noqa: E501

        Returns the specified segment.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_segment_by_id_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the segment. (required)
        :return: DetailedSegment
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_segment_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_segment_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['strava_oauth']  # noqa: E501

        return self.api_client.call_api(
            '/segments/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DetailedSegment',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def star_segment(self, id, starred, **kwargs):  # noqa: E501
        """Star Segment  # noqa: E501

        Stars/Unstars the given segment for the authenticated athlete.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.star_segment(id, starred, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the segment to star. (required)
        :param bool starred: If true, star the segment; if false, unstar the segment. (required)
        :return: DetailedSegment
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.star_segment_with_http_info(id, starred, **kwargs)  # noqa: E501
        else:
            (data) = self.star_segment_with_http_info(id, starred, **kwargs)  # noqa: E501
            return data

    def star_segment_with_http_info(self, id, starred, **kwargs):  # noqa: E501
        """Star Segment  # noqa: E501

        Stars/Unstars the given segment for the authenticated athlete.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.star_segment_with_http_info(id, starred, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the segment to star. (required)
        :param bool starred: If true, star the segment; if false, unstar the segment. (required)
        :return: DetailedSegment
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'starred']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method star_segment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `star_segment`")  # noqa: E501
        # verify the required parameter 'starred' is set
        if ('starred' not in params or
                params['starred'] is None):
            raise ValueError("Missing the required parameter `starred` when calling `star_segment`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'starred' in params:
            form_params.append(('starred', params['starred']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['strava_oauth']  # noqa: E501

        return self.api_client.call_api(
            '/segments/{id}/starred', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DetailedSegment',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
