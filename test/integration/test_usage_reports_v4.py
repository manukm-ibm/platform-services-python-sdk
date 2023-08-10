# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2023.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Integration Tests for UsageReportsV4
"""

from ibm_cloud_sdk_core import *
import os
import pytest
from ibm_platform_services.usage_reports_v4 import *

# Config file name
config_file = 'usage_reports_v4.env'


class TestUsageReportsV4:
    """
    Integration Test Class for UsageReportsV4
    """

    @classmethod
    def setup_class(cls):
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            cls.usage_reports_service = UsageReportsV4.new_instance(
            )
            assert cls.usage_reports_service is not None

            cls.config = read_external_sources(UsageReportsV4.DEFAULT_SERVICE_NAME)
            assert cls.config is not None

            cls.usage_reports_service.enable_retries()

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_get_account_summary(self):
        response = self.usage_reports_service.get_account_summary(
            account_id='testString',
            billingmonth='testString',
            accept='application/json',
            format='csv',
        )

        assert response.get_status_code() == 200
        account_summary = response.get_result()
        assert account_summary is not None

    @needscredentials
    def test_get_account_usage(self):
        response = self.usage_reports_service.get_account_usage(
            account_id='testString',
            billingmonth='testString',
            names=True,
            accept_language='testString',
        )

        assert response.get_status_code() == 200
        account_usage = response.get_result()
        assert account_usage is not None

    @needscredentials
    def test_get_resource_group_usage(self):
        response = self.usage_reports_service.get_resource_group_usage(
            account_id='testString',
            resource_group_id='testString',
            billingmonth='testString',
            names=True,
            accept_language='testString',
        )

        assert response.get_status_code() == 200
        resource_group_usage = response.get_result()
        assert resource_group_usage is not None

    @needscredentials
    def test_get_resource_usage_account(self):
        response = self.usage_reports_service.get_resource_usage_account(
            account_id='testString',
            billingmonth='testString',
            accept='application/json',
            format='csv',
            names=True,
            tags=True,
            accept_language='testString',
            limit=30,
            start='testString',
            resource_group_id='testString',
            organization_id='testString',
            resource_instance_id='testString',
            resource_id='testString',
            plan_id='testString',
            region='testString',
        )

        assert response.get_status_code() == 200
        instances_usage = response.get_result()
        assert instances_usage is not None

    @needscredentials
    def test_get_resource_usage_account_with_pager(self):
        all_results = []

        # Test get_next().
        pager = GetResourceUsageAccountPager(
            client=self.usage_reports_service,
            account_id='testString',
            billingmonth='testString',
            accept='application/json',
            format='csv',
            names=True,
            tags=True,
            accept_language='testString',
            limit=30,
            resource_group_id='testString',
            organization_id='testString',
            resource_instance_id='testString',
            resource_id='testString',
            plan_id='testString',
            region='testString',
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)

        # Test get_all().
        pager = GetResourceUsageAccountPager(
            client=self.usage_reports_service,
            account_id='testString',
            billingmonth='testString',
            accept='application/json',
            format='csv',
            names=True,
            tags=True,
            accept_language='testString',
            limit=30,
            resource_group_id='testString',
            organization_id='testString',
            resource_instance_id='testString',
            resource_id='testString',
            plan_id='testString',
            region='testString',
        )
        all_items = pager.get_all()
        assert all_items is not None

        assert len(all_results) == len(all_items)
        print(f'\nget_resource_usage_account() returned a total of {len(all_results)} items(s) using GetResourceUsageAccountPager.')

    @needscredentials
    def test_get_resource_usage_resource_group(self):
        response = self.usage_reports_service.get_resource_usage_resource_group(
            account_id='testString',
            resource_group_id='testString',
            billingmonth='testString',
            names=True,
            tags=True,
            accept_language='testString',
            limit=30,
            start='testString',
            resource_instance_id='testString',
            resource_id='testString',
            plan_id='testString',
            region='testString',
        )

        assert response.get_status_code() == 200
        instances_usage = response.get_result()
        assert instances_usage is not None

    @needscredentials
    def test_get_resource_usage_resource_group_with_pager(self):
        all_results = []

        # Test get_next().
        pager = GetResourceUsageResourceGroupPager(
            client=self.usage_reports_service,
            account_id='testString',
            resource_group_id='testString',
            billingmonth='testString',
            names=True,
            tags=True,
            accept_language='testString',
            limit=30,
            resource_instance_id='testString',
            resource_id='testString',
            plan_id='testString',
            region='testString',
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)

        # Test get_all().
        pager = GetResourceUsageResourceGroupPager(
            client=self.usage_reports_service,
            account_id='testString',
            resource_group_id='testString',
            billingmonth='testString',
            names=True,
            tags=True,
            accept_language='testString',
            limit=30,
            resource_instance_id='testString',
            resource_id='testString',
            plan_id='testString',
            region='testString',
        )
        all_items = pager.get_all()
        assert all_items is not None

        assert len(all_results) == len(all_items)
        print(f'\nget_resource_usage_resource_group() returned a total of {len(all_results)} items(s) using GetResourceUsageResourceGroupPager.')

    @needscredentials
    def test_get_resource_usage_org(self):
        response = self.usage_reports_service.get_resource_usage_org(
            account_id='testString',
            organization_id='testString',
            billingmonth='testString',
            names=True,
            tags=True,
            accept_language='testString',
            limit=30,
            start='testString',
            resource_instance_id='testString',
            resource_id='testString',
            plan_id='testString',
            region='testString',
        )

        assert response.get_status_code() == 200
        instances_usage = response.get_result()
        assert instances_usage is not None

    @needscredentials
    def test_get_resource_usage_org_with_pager(self):
        all_results = []

        # Test get_next().
        pager = GetResourceUsageOrgPager(
            client=self.usage_reports_service,
            account_id='testString',
            organization_id='testString',
            billingmonth='testString',
            names=True,
            tags=True,
            accept_language='testString',
            limit=30,
            resource_instance_id='testString',
            resource_id='testString',
            plan_id='testString',
            region='testString',
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)

        # Test get_all().
        pager = GetResourceUsageOrgPager(
            client=self.usage_reports_service,
            account_id='testString',
            organization_id='testString',
            billingmonth='testString',
            names=True,
            tags=True,
            accept_language='testString',
            limit=30,
            resource_instance_id='testString',
            resource_id='testString',
            plan_id='testString',
            region='testString',
        )
        all_items = pager.get_all()
        assert all_items is not None

        assert len(all_results) == len(all_items)
        print(f'\nget_resource_usage_org() returned a total of {len(all_results)} items(s) using GetResourceUsageOrgPager.')

    @needscredentials
    def test_get_org_usage(self):
        response = self.usage_reports_service.get_org_usage(
            account_id='testString',
            organization_id='testString',
            billingmonth='testString',
            names=True,
            accept_language='testString',
        )

        assert response.get_status_code() == 200
        org_usage = response.get_result()
        assert org_usage is not None

    @needscredentials
    def test_create_reports_snapshot_config(self):
        response = self.usage_reports_service.create_reports_snapshot_config(
            account_id='abc',
            interval='daily',
            cos_bucket='bucket_name',
            cos_location='us-south',
            cos_reports_folder='IBMCloud-Billing-Reports',
            report_types=['account_summary', 'enterprise_summary', 'account_resource_instance_usage'],
            versioning='new',
        )

        assert response.get_status_code() == 201
        snapshot_config = response.get_result()
        assert snapshot_config is not None

    @needscredentials
    def test_update_reports_snapshot_config(self):
        response = self.usage_reports_service.update_reports_snapshot_config(
            account_id='abc',
            interval='daily',
            cos_bucket='bucket_name',
            cos_location='us-south',
            cos_reports_folder='IBMCloud-Billing-Reports',
            report_types=['account_summary', 'enterprise_summary', 'account_resource_instance_usage'],
            versioning='new',
        )

        assert response.get_status_code() == 200
        snapshot_config = response.get_result()
        assert snapshot_config is not None

    @needscredentials
    def test_get_reports_snapshot_config(self):
        response = self.usage_reports_service.get_reports_snapshot_config(
            account_id='abc',
        )

        assert response.get_status_code() == 200
        snapshot_config = response.get_result()
        assert snapshot_config is not None

    @needscredentials
    def test_get_reports_snapshot(self):
        response = self.usage_reports_service.get_reports_snapshot(
            account_id='abc',
            month='2023-02',
            date_from=1675209600000,
            date_to=1675987200000,
        )

        assert response.get_status_code() == 200
        snapshot_list = response.get_result()
        assert snapshot_list is not None

    @needscredentials
    def test_delete_reports_snapshot_config(self):
        response = self.usage_reports_service.delete_reports_snapshot_config(
            account_id='abc',
        )

        assert response.get_status_code() == 204
