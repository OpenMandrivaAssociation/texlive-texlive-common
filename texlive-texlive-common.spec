# revision 26673
# category TLCore
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-texlive-common
Version:	20120808
Release:	1
Summary:	TeX Live documentation (common elements)
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texlive-common.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texlive-common.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
TeXLive texlive-common package.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdir}/doc/texlive/index.html
%doc %{_texmfdir}/doc/texlive/texlive-common/examples/ex5.tex
%doc %{_texmfdir}/doc/texlive/texlive-common/examples/ex6.tex
%doc %{_texmfdir}/doc/texlive/texlive-common/examples/ex6a.tex
%doc %{_texmfdir}/doc/texlive/texlive-common/examples/ex6b.tex
%doc %{_texmfdir}/doc/texlive/texlive-common/examples/ex6c.tex
%doc %{_texmfdir}/doc/texlive/texlive-common/install-lnx-main.png
%doc %{_texmfdir}/doc/texlive/texlive-common/psview.png
%doc %{_texmfdir}/doc/texlive/texlive-common/stdcoll.png
%doc %{_texmfdir}/doc/texlive/texlive-common/tlmgr-general-options.png
%doc %{_texmfdir}/doc/texlive/texlive-common/tlmgr-gui.png
%doc %{_texmfdir}/doc/texlive/texlive-common/tlmgr-paper-options.png
%doc %{_texmfdir}/doc/texlive/texlive-common/tray-menu.png
%doc %{_texmfdir}/doc/texlive/texlive-common/wizard-w32.png

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf %{buildroot}%{_datadir}


%changelog
* Wed Aug 08 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120808-1
+ Revision: 812898
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20111104-2
+ Revision: 756628
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111104-1
+ Revision: 719691
- texlive-texlive-common
- texlive-texlive-common
- texlive-texlive-common
- texlive-texlive-common

