#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Encode-JIS2K
Version  : 0.03
Release  : 2
URL      : https://cpan.metacpan.org/authors/id/D/DA/DANKOGAI/Encode-JIS2K-0.03.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DA/DANKOGAI/Encode-JIS2K-0.03.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libe/libencode-jis2k-perl/libencode-jis2k-perl_0.03-1.debian.tar.xz
Summary  : unknown
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-Encode-JIS2K-lib = %{version}-%{release}
Requires: perl-Encode-JIS2K-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
Encode::JIS2K - JIS X 0212 (aka JIS 2000) Encodings
INSTALLATION
To install this module type the following:

%package lib
Summary: lib components for the perl-Encode-JIS2K package.
Group: Libraries
Requires: perl-Encode-JIS2K-license = %{version}-%{release}

%description lib
lib components for the perl-Encode-JIS2K package.


%package license
Summary: license components for the perl-Encode-JIS2K package.
Group: Default

%description license
license components for the perl-Encode-JIS2K package.


%prep
%setup -q -n Encode-JIS2K-0.03
cd ..
%setup -q -T -D -n Encode-JIS2K-0.03 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Encode-JIS2K-0.03/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Encode-JIS2K
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-Encode-JIS2K/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.26.1/x86_64-linux-thread-multi/Encode/JIS2K.pm
/usr/lib/perl5/vendor_perl/5.26.1/x86_64-linux-thread-multi/Encode/JIS2K/2022JP3.pm

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.26.1/x86_64-linux-thread-multi/auto/Encode/JIS2K/JIS2K.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Encode-JIS2K/deblicense_copyright
