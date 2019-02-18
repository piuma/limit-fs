Name:           limit-fs
Version:        0.1
Release:        1%{?dist}
Summary:        FUSE filesystem that removes the oldest file whenever the free space reaches limits

Group:          System Environment/Kernel
License:        GPL+
URL:            https://github.com/piuma/limit-fs
Source:         %{name}-%{version}.tar.gz

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:  glib2-devel

%if 0%{?fedora} >= 27
BuildRequires:  fuse3-devel >= 3
Requires:       fuse3
%else
BuildRequires:  fuse-devel
Requires:       fuse
%endif

Obsoletes:      limit-fs <= %{version}-%{release}
Provides:       limit-fs = %{version}-%{release}

%description
This is a FUSE filesystem that removes the oldest files whenever the
free space reaches the set percentage.

You can use it in a no empty directory, anything you write in will be
written in the underlying filesystem. After unmounting it all files
remain in the unmounted directory.
 
%prep
%setup -q -n %{name}-%{version}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf  %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/limit-fs

%changelog
* Tue Feb 12 2019 Danilo Abbasciano <danilo@piumalab.org> 0.1
- initial RPM package.

