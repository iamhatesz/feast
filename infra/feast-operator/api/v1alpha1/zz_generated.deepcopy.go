//go:build !ignore_autogenerated

/*
Copyright 2024 Feast Community.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/

// Code generated by controller-gen. DO NOT EDIT.

package v1alpha1

import (
	"k8s.io/api/core/v1"
	metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
	runtime "k8s.io/apimachinery/pkg/runtime"
)

// DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.
func (in *DefaultConfigs) DeepCopyInto(out *DefaultConfigs) {
	*out = *in
	if in.Image != nil {
		in, out := &in.Image, &out.Image
		*out = new(string)
		**out = **in
	}
}

// DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new DefaultConfigs.
func (in *DefaultConfigs) DeepCopy() *DefaultConfigs {
	if in == nil {
		return nil
	}
	out := new(DefaultConfigs)
	in.DeepCopyInto(out)
	return out
}

// DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.
func (in *FeatureStore) DeepCopyInto(out *FeatureStore) {
	*out = *in
	out.TypeMeta = in.TypeMeta
	in.ObjectMeta.DeepCopyInto(&out.ObjectMeta)
	in.Spec.DeepCopyInto(&out.Spec)
	in.Status.DeepCopyInto(&out.Status)
}

// DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new FeatureStore.
func (in *FeatureStore) DeepCopy() *FeatureStore {
	if in == nil {
		return nil
	}
	out := new(FeatureStore)
	in.DeepCopyInto(out)
	return out
}

// DeepCopyObject is an autogenerated deepcopy function, copying the receiver, creating a new runtime.Object.
func (in *FeatureStore) DeepCopyObject() runtime.Object {
	if c := in.DeepCopy(); c != nil {
		return c
	}
	return nil
}

// DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.
func (in *FeatureStoreList) DeepCopyInto(out *FeatureStoreList) {
	*out = *in
	out.TypeMeta = in.TypeMeta
	in.ListMeta.DeepCopyInto(&out.ListMeta)
	if in.Items != nil {
		in, out := &in.Items, &out.Items
		*out = make([]FeatureStore, len(*in))
		for i := range *in {
			(*in)[i].DeepCopyInto(&(*out)[i])
		}
	}
}

// DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new FeatureStoreList.
func (in *FeatureStoreList) DeepCopy() *FeatureStoreList {
	if in == nil {
		return nil
	}
	out := new(FeatureStoreList)
	in.DeepCopyInto(out)
	return out
}

// DeepCopyObject is an autogenerated deepcopy function, copying the receiver, creating a new runtime.Object.
func (in *FeatureStoreList) DeepCopyObject() runtime.Object {
	if c := in.DeepCopy(); c != nil {
		return c
	}
	return nil
}

// DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.
func (in *FeatureStoreRef) DeepCopyInto(out *FeatureStoreRef) {
	*out = *in
}

// DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new FeatureStoreRef.
func (in *FeatureStoreRef) DeepCopy() *FeatureStoreRef {
	if in == nil {
		return nil
	}
	out := new(FeatureStoreRef)
	in.DeepCopyInto(out)
	return out
}

// DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.
func (in *FeatureStoreServices) DeepCopyInto(out *FeatureStoreServices) {
	*out = *in
	if in.OfflineStore != nil {
		in, out := &in.OfflineStore, &out.OfflineStore
		*out = new(OfflineStore)
		(*in).DeepCopyInto(*out)
	}
	if in.OnlineStore != nil {
		in, out := &in.OnlineStore, &out.OnlineStore
		*out = new(OnlineStore)
		(*in).DeepCopyInto(*out)
	}
	if in.Registry != nil {
		in, out := &in.Registry, &out.Registry
		*out = new(Registry)
		(*in).DeepCopyInto(*out)
	}
}

// DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new FeatureStoreServices.
func (in *FeatureStoreServices) DeepCopy() *FeatureStoreServices {
	if in == nil {
		return nil
	}
	out := new(FeatureStoreServices)
	in.DeepCopyInto(out)
	return out
}

// DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.
func (in *FeatureStoreSpec) DeepCopyInto(out *FeatureStoreSpec) {
	*out = *in
	if in.Services != nil {
		in, out := &in.Services, &out.Services
		*out = new(FeatureStoreServices)
		(*in).DeepCopyInto(*out)
	}
}

// DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new FeatureStoreSpec.
func (in *FeatureStoreSpec) DeepCopy() *FeatureStoreSpec {
	if in == nil {
		return nil
	}
	out := new(FeatureStoreSpec)
	in.DeepCopyInto(out)
	return out
}

// DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.
func (in *FeatureStoreStatus) DeepCopyInto(out *FeatureStoreStatus) {
	*out = *in
	in.Applied.DeepCopyInto(&out.Applied)
	if in.Conditions != nil {
		in, out := &in.Conditions, &out.Conditions
		*out = make([]metav1.Condition, len(*in))
		for i := range *in {
			(*in)[i].DeepCopyInto(&(*out)[i])
		}
	}
	out.ServiceHostnames = in.ServiceHostnames
}

// DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new FeatureStoreStatus.
func (in *FeatureStoreStatus) DeepCopy() *FeatureStoreStatus {
	if in == nil {
		return nil
	}
	out := new(FeatureStoreStatus)
	in.DeepCopyInto(out)
	return out
}

// DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.
func (in *LocalRegistryConfig) DeepCopyInto(out *LocalRegistryConfig) {
	*out = *in
	in.ServiceConfigs.DeepCopyInto(&out.ServiceConfigs)
}

// DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new LocalRegistryConfig.
func (in *LocalRegistryConfig) DeepCopy() *LocalRegistryConfig {
	if in == nil {
		return nil
	}
	out := new(LocalRegistryConfig)
	in.DeepCopyInto(out)
	return out
}

// DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.
func (in *OfflineStore) DeepCopyInto(out *OfflineStore) {
	*out = *in
	in.ServiceConfigs.DeepCopyInto(&out.ServiceConfigs)
}

// DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new OfflineStore.
func (in *OfflineStore) DeepCopy() *OfflineStore {
	if in == nil {
		return nil
	}
	out := new(OfflineStore)
	in.DeepCopyInto(out)
	return out
}

// DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.
func (in *OnlineStore) DeepCopyInto(out *OnlineStore) {
	*out = *in
	in.ServiceConfigs.DeepCopyInto(&out.ServiceConfigs)
}

// DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new OnlineStore.
func (in *OnlineStore) DeepCopy() *OnlineStore {
	if in == nil {
		return nil
	}
	out := new(OnlineStore)
	in.DeepCopyInto(out)
	return out
}

// DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.
func (in *OptionalConfigs) DeepCopyInto(out *OptionalConfigs) {
	*out = *in
	if in.ImagePullPolicy != nil {
		in, out := &in.ImagePullPolicy, &out.ImagePullPolicy
		*out = new(v1.PullPolicy)
		**out = **in
	}
	if in.Resources != nil {
		in, out := &in.Resources, &out.Resources
		*out = new(v1.ResourceRequirements)
		(*in).DeepCopyInto(*out)
	}
}

// DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new OptionalConfigs.
func (in *OptionalConfigs) DeepCopy() *OptionalConfigs {
	if in == nil {
		return nil
	}
	out := new(OptionalConfigs)
	in.DeepCopyInto(out)
	return out
}

// DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.
func (in *Registry) DeepCopyInto(out *Registry) {
	*out = *in
	if in.Local != nil {
		in, out := &in.Local, &out.Local
		*out = new(LocalRegistryConfig)
		(*in).DeepCopyInto(*out)
	}
	if in.Remote != nil {
		in, out := &in.Remote, &out.Remote
		*out = new(RemoteRegistryConfig)
		(*in).DeepCopyInto(*out)
	}
}

// DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new Registry.
func (in *Registry) DeepCopy() *Registry {
	if in == nil {
		return nil
	}
	out := new(Registry)
	in.DeepCopyInto(out)
	return out
}

// DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.
func (in *RemoteRegistryConfig) DeepCopyInto(out *RemoteRegistryConfig) {
	*out = *in
	if in.Hostname != nil {
		in, out := &in.Hostname, &out.Hostname
		*out = new(string)
		**out = **in
	}
	if in.FeastRef != nil {
		in, out := &in.FeastRef, &out.FeastRef
		*out = new(FeatureStoreRef)
		**out = **in
	}
}

// DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new RemoteRegistryConfig.
func (in *RemoteRegistryConfig) DeepCopy() *RemoteRegistryConfig {
	if in == nil {
		return nil
	}
	out := new(RemoteRegistryConfig)
	in.DeepCopyInto(out)
	return out
}

// DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.
func (in *ServiceConfigs) DeepCopyInto(out *ServiceConfigs) {
	*out = *in
	in.DefaultConfigs.DeepCopyInto(&out.DefaultConfigs)
	in.OptionalConfigs.DeepCopyInto(&out.OptionalConfigs)
}

// DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new ServiceConfigs.
func (in *ServiceConfigs) DeepCopy() *ServiceConfigs {
	if in == nil {
		return nil
	}
	out := new(ServiceConfigs)
	in.DeepCopyInto(out)
	return out
}

// DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.
func (in *ServiceHostnames) DeepCopyInto(out *ServiceHostnames) {
	*out = *in
}

// DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new ServiceHostnames.
func (in *ServiceHostnames) DeepCopy() *ServiceHostnames {
	if in == nil {
		return nil
	}
	out := new(ServiceHostnames)
	in.DeepCopyInto(out)
	return out
}
