#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-Encode-JIS2K
Version  : 0.05
Release  : 31
URL      : https://cpan.metacpan.org/authors/id/D/DA/DANKOGAI/Encode-JIS2K-0.05.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DA/DANKOGAI/Encode-JIS2K-0.05.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libe/libencode-jis2k-perl/libencode-jis2k-perl_0.03-1.debian.tar.xz
Summary  : unknown
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-Encode-JIS2K-license = %{version}-%{release}
Requires: perl-Encode-JIS2K-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
Encode::JIS2K - JIS X 0212 (aka JIS 2000) Encodings
SYNOPSIS
use Encode::JIS2K;
use Encode qw/encode decode/;
$euc_2k = encode("euc-jisx0213", $utf8);
$utf8   = decode("euc-jisx0213", $euc_jp);

%package license
Summary: license components for the perl-Encode-JIS2K package.
Group: Default

%description license
license components for the perl-Encode-JIS2K package.


%package perl
Summary: perl components for the perl-Encode-JIS2K package.
Group: Default
Requires: perl-Encode-JIS2K = %{version}-%{release}

%description perl
perl components for the perl-Encode-JIS2K package.


%prep
%setup -q -n Encode-JIS2K-0.05
cd %{_builddir}
tar xf %{_sourcedir}/libencode-jis2k-perl_0.03-1.debian.tar.xz
cd %{_builddir}/Encode-JIS2K-0.05
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Encode-JIS2K-0.05/deblicense/
pushd ..
cp -a Encode-JIS2K-0.05 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Encode-JIS2K
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Encode-JIS2K/017e59e9f8775668d9c004454085fb7d939fc997 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Encode-JIS2K/017e59e9f8775668d9c004454085fb7d939fc997

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
