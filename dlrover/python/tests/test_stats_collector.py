# Copyright 2022 The DLRover Authors. All rights reserved.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import time
import unittest

from dlrover.python.common.constants import NodeType
from dlrover.python.master.monitor.speed_monitor import SpeedMonitor
from dlrover.python.master.node_watcher.base_watcher import Node
from dlrover.python.master.stats_collector.job_collector import (
    JobMetricCollector,
)
from dlrover.python.master.stats_collector.reporter import (
    JobMeta,
    LocalStatsReporter,
)
from dlrover.python.master.stats_collector.training_metrics import (
    RuntimeMetric,
)


class LocalStatsCollectorTest(unittest.TestCase):
    def test_report_resource_usage(self):
        job_meta = JobMeta("1111")
        collector = LocalStatsReporter(job_meta)

        collector.report_runtime_stats(RuntimeMetric([]))
        collector.report_runtime_stats(RuntimeMetric([]))
        self.assertEqual(len(collector._runtime_stats), 2)


class StatsCollectorTest(unittest.TestCase):
    def test_job_metric_collector(self):
        job_meta = JobMeta("1111")
        collector = JobMetricCollector(job_meta)
        collector.report_dataset_metric("test", 1000)

        speed_monitor = SpeedMonitor()
        t = int(time.time())
        speed_monitor.sample_global_step(100, t)
        speed_monitor.sample_global_step(1100, t + 10)
        speed_monitor.add_running_worker(0)
        worker = Node(NodeType.WORKER, 0)
        collector.set_runtime_info(speed_monitor, [worker])
        self.assertEqual(len(collector._runtime_metric.running_pods), 1)
        self.assertEqual(collector._runtime_metric.speed, 100)
        self.assertEqual(len(collector._stats_collector._runtime_stats), 1)