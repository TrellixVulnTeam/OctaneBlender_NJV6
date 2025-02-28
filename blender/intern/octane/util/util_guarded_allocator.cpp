/*
 * Copyright 2011-2015 Blender Foundation
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#include "util/util_guarded_allocator.h"
#include "util/util_stats.h"

OCT_NAMESPACE_BEGIN

static Stats global_stats(Stats::static_init);

/* Internal API. */

void util_guarded_mem_alloc(size_t n)
{
  global_stats.mem_alloc(n);
}

void util_guarded_mem_free(size_t n)
{
  global_stats.mem_free(n);
}

/* Public API. */

size_t util_guarded_get_mem_used()
{
  return global_stats.mem_used;
}

size_t util_guarded_get_mem_peak()
{
  return global_stats.mem_peak;
}

OCT_NAMESPACE_END
